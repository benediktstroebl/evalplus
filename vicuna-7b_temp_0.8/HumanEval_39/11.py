

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
    # n must be odd
    if not (n % 2 == 0):
        return 1

    # if n is 1 or 2, then we are done
    if n == 1:
        return 1
    elif n == 2:
        return 2

    # fibonacci sequence
    a, b = 0, 1
    for _ in range(n-2):
        a, b = b, a + b

    # check primality
    if a % 2 == 0 or b % 2 == 0:
        return 1
    else:
        for _ in range(n-1):
            if a % 2 == 0 or b % 2 == 0:
                if is_prime(a) and is_prime(b):
                    return a * b
        return 1
