#!/usr/bin/env python

# WS server example

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"input: {name}")

    greeting = f"Hello {name} from server!"

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, 'localhost', 8765)

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(start_server)
    loop.run_forever()
except KeyboardInterrupt:
    pass