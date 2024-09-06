```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    sequence = [2]
    sqrt_n = int(math.sqrt(n))
    for _ in range(2, sqrt_n + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(i)) + 1):
            if i % _ == 0:
                is_prime = False
                break
        if is_prime:
            sequence.append(i)
    return next(sequence)
```

This script defines a function `prime_fib` which computes the nth Fibonacci number and checks if it is prime, where `n` is the integer for which the function is being called. The function uses a sequence approach to find the prime factor of numbers. The function raises a ValueError exception if n is not a positive integer.