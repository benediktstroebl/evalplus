

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
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        # Check if the number is prime
        if n % 2 == 0:
            return 0
        if n % 3 == 0:
            return 0
        for x in range(1, int(n**0.5) + 1):
            if n % x == 0:
                return 0
        return 1
