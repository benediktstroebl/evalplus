from itertools import count
import math
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n should be a positive integer.")

    def fib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    pf_iter = fib()
    num = next(pf_iter)
    idx = 0

    for _ in count(n):
        num = next(pf_iter)
        if is_prime(num):
            idx += 1
        if idx == n:
            return num