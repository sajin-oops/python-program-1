import asyncio
async def say_hello():
    print("Hello")
    await asyncio.sleep(6)
    print("World")

async def main():
    await say_hello()
asyncio.run(main())

'''
O/P

Hello
World
'''