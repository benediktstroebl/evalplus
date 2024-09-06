from itertools import count
import math
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    while len(fib) > n:
        fib.pop()
    return fib[n - 1]