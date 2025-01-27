import asyncio
import websockets
import json

async def test_websocket():
    uri = "ws://10.30.1.221:8010/ws/sniff/"
    async with websockets.connect(uri) as websocket:
        # Send initial data to start the tcpdump command
        message = json.dumps({
            'pod_name': 'oai-cu-level1-user2-6864489f7-st9hj',  # Replace with your actual pod name
            'namespace': 'user2'  # Replace with your actual namespace
        })
        await websocket.send(message)
        
        # Listen for messages from the server
        while True:
            try:
                response = await websocket.recv()
                response_data = json.loads(response)
                if 'data' in response_data:
                    print(response_data['data'])
                elif 'message' in response_data:
                    print(response_data['message'])
            except websockets.ConnectionClosed:
                print("Connection closed")
                break

# Replace 'your_pod_name' and 'your_namespace' with actual values
asyncio.get_event_loop().run_until_complete(test_websocket())
