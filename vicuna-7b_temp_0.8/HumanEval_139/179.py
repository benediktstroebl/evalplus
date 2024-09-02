
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    n = asyncio.get_event_loop().run_until_complete(int(n))
    return n * (n - 1) * (n - 2) * ... * (n - 5) * (n - 4) * (n - 3) * (n - 2) * (n - 1) * 1

async def main():
    loop = asyncio.get_event_loop()
    for i in range(10):
        await loop.run_in_executor(None, special_factorial)

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()