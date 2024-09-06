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
    term = 0
    num = next(count(start=2, step=2))

    while len(fib) < n:
        num = next(count(start=num, step=2))
        fib.append(num)
        term += num
    
    # We make sure the returned number is prime by iterating through the numbers starting from it
    # Until we find a number which divides it evenly or reaches the starting number
    for i in count(term, 2):
        if is_prime(i):
            return i