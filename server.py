#!/usr/bin/env python

# WS server example

import asyncio
import websockets

loop = asyncio.get_event_loop()

async def hello(websocket, path):
    try:
        name = await websocket.recv()
        print(f"input: {name}")

        greeting = f"Hello {name} from server!"

        await websocket.send(greeting)
        print(f"> {greeting}")
    except websockets.ConnectionClosed:
        print("connection closed")

start_server = websockets.serve(hello, 'localhost', 8765)


try:
    loop.run_until_complete(start_server)
    loop.run_forever()
except KeyboardInterrupt:
    pass