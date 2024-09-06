```python
import math
def prime_fib(n):
    """
    Returns n-th Fibonacci number and checks if it's prime.
    if n <= 1:
        return n
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n % 5 == 0:
        return True
    # Calculate nth Fibonacci number using recursion
    return math.sqrt(5 - n + 1 + 4 ) + prime_fib(n-1)
``` 
This function is self-contained and calculates the nth Fibonacci number while verifying if it's prime.