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
        a = prime_fib(n // 2)
        b = 2
        for _ in range(2, n // 2):
            if math.isq(a + b) == n:
                break
            b += 1
        return b
``` 
This function calculates the n-th Fibonacci number that is also prime using prime factorization. It uses a maximum recursive approach to solve this problem.