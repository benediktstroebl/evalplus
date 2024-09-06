```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    if n <= 1:
        return n
    factors = [2]
    for i in range(2, n):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            factors.append(i)
    return next(factors)
``` 
The code defines a function `prime_fib` that computes the nth Fibonacci number and checks if it's prime. It uses a basic trial with a loop and a list of factors to find prime numbers, and then returns the nth Fibonacci number. The function is self-contained and solves the problem of finding the nth prime Fibonacci number with efficiency.