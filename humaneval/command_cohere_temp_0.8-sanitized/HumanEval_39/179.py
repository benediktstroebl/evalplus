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
    fa = 2
    md = 300

    for _ in count(md):
        fn = fib[-1]
        fib.append(fn)
        if is_prime(fib[-1]):
            fa = fib[-1]
            break
    
    idx = 0
    while fib[idx] < n:
        idx += 1

    # calculate the nth Fibonacci number
    n_fib = fib[idx - 1]
    for _ in range(n - n_fib):
        fa, n_fib = n_fib, fa + n_fib
    
    return n_fib