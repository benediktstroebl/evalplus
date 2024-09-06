from itertools import count
import math
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    
    fib = [0, 1]
    curr_num = 2
    count = count(fib[1])
    
    for _ in range(n - 1):
        next_num = curr_num + count()
        fib.append(next_num)
        curr_num = next_num
    
    # Search for the nth Fibonacci number in the sequence
    while len(fib) <= n:
        fib.append(curr_num)
        curr_num = curr_num + count()
    
    return fib[n]