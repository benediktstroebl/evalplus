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
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        raise ValueError("n must be positive")

    fib = [0, 1]
    x, y = fib[0], fib[1]
    for _ in count(n - 1):
        x, y = y, x + y

    # Starting from the (n-1)th Fibonacci number,
    # we iterate through the Fibonacci sequence,
    # checking each number for primality until we find the n-th prime Fibonacci number.
    while x < n:
        if is_prime(x):
            n -= 1
        x, y = y, x + y

    return x