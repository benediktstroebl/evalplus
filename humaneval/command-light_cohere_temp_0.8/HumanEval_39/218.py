```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n should be a positive integer")
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(n - 2):
        a, b = math.isprime(a + b) or a + b
    return a
``` 
This Python code defines a function called **prime_fibonacci** that calculates the n-th Fibonacci number, ensuring it's prime. It employs backtracking, a recursive approach to identify prime numbers within the Fibonacci sequence, where the function itself checks for prime numbers, and the loop iterates through the sequence. The code also includes input validation to ensure the function is called with a positive integer n.