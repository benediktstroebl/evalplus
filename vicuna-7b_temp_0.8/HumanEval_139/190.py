
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
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

async def main():
    loop = asyncio.get_event_loop()
    # ...

    @loop.create_task
    async def my_task():
        await asyncio.wait([
            loop.create_task(special_factorial(42)),
            loop.create_task(special_factorial(150)),
            loop.create_task(special_factorial(365))
        ], return_when=asyncio.FIRST_COMPLETED)

    loop.run_until_complete(my_task)
    loop.close()
