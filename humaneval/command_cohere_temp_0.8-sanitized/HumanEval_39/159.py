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
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev_fib, curr_fib = 0, 1
    num = next((fib for fib in count(prev_fib, step=curr_fib) if is_prime(fib)), -1)
    return num