

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    # base case
    if n < 2:
        return 2

    # check if n is prime
    if n % 2 == 0 or n % 3 == 0:
        return 0

    # calculate fibonacci number
    previous = 0
    current = 1
    for _ in range(n // 2):
        current += previous
        previous = current

    # check if number is prime
    if current - 2 in [p - 2 for p in range(2, n + 1)]:
        return current - 2

    # return number
    return current - 2
