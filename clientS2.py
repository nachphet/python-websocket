#!/usr/bin/env python3

import asyncio
import websockets
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

async def logIn(uri, myjson):
    async with websockets.connect(uri) as websocket:
        await websocket.send(myjson)

async def logIn(uri, myjson):
    async with websockets.connect(uri, ssl=ssl_context) as websocket:
        await websocket.send(myjson)
        resp = await websocket.recv()
        print(resp)

#myurl = f"wss://{args.server}:{args.port}"
myurl = "wss://localhost:8765"
print("connection url:{}".format(myurl))

# logdef is the json string I send in
asyncio.get_event_loop().run_until_complete(
    logIn(myurl, "12312")
)