from itertools import count, takewhile
def is_prime(n):
    """
    Checks if number is prime
    :param n: number to be checked
    :return: boolean
    """
    return n > 1 and all(n % i for i in range(3, int(n ** 0.5) + 1, 2))
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    :param n: target number
    :return: integer
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n should be a positive integer.")
    a, b = 2, 3
    cnt = count(max(1000, 2 * n), step=2)
    return next(takewhile(lambda x: is_prime(x), cnt), -1)