#!/usr/bin/env python

# WS client example

import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:
        name = input("What's your name? ")

        await websocket.send(name)

        greeting = await websocket.recv()
        print(f"< {greeting}")

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())