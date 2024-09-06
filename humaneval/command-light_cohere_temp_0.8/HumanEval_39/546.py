```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        limit = math.N(n**2)
        for i in range(3, limit, 2):
            if math.isprime(i):
                yield i
        else:
            break
    
    return -1  # To avoid an infinite loop
``` 
This code defines a Python function that computes and returns the n-th Fibonacci number that is prime. It also tests for its factoriality of the generated numbers.