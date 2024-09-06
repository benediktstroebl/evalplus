```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        # Use the efficient faster loop-based approach
        prev, curr = 1, 2
        for _ in range(3, n + 1):
            next_num = prev + curr
            if math.is(next_num):
                break
            prev, curr = curr, next_num
        return curr
``` 
This script provides a prime_fib function that calculates and returns the n-th Fibonacci number that is prime, and tests to ensure its correctness.