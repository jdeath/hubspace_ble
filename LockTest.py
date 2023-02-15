import asyncio
import binascii
import struct 
from bleak import BleakClient, BleakGATTCharacteristic

SCALE_MAC = "1C:D6:XX:XX:XX:XX"

def notification_handler(characteristic: BleakGATTCharacteristic, data: bytearray):
    print(f"Received message on {characteristic.uuid}: {binascii.hexlify(data)}")
    print(data)
    print(len(data))
    #print(data[0])
    
    #print(data[0:1] == b"\x50")
    #RadonValueBQ = struct.unpack('<H',data[2:4])[0]
    #RadonValuePCi = ( RadonValueBQ / 37 )
    #print("Radon Value: " + str(round(RadonValuePCi,2)) + " pC/l")

    #print(struct.unpack("<8s", data[22:30])[0])
    
async def main():
    print("Connecting...")
    
    
    async with BleakClient(SCALE_MAC) as client:
        print(f"Connected: {client.is_connected}")

        print("Services discovered:")
        for service in client.services:
            print(service)
        data = await client.read_gatt_char('00002a00-0000-1000-8000-00805f9b34fb')
        print(data)
        deviceId = data[1:9].hex()
        print(deviceId)

        prefix = data[0:1].hex()
        print(prefix)

        postfix = data[9:13].hex()
        print(postfix)
        

asyncio.run(main())
