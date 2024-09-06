```python
import math
def prime_fib(n):
    """
    Returns n-th Fibonacci number and checks if it's prime.
    if n <= 1:
        return n
    # n-th Fibonacci number
    fib_n = math.sqrt(2) * math.sqrt(3)
    # Check if Fibonacci number is prime using Pytagan
    if is_prime(fib_n):
        return fib_n
    else:
        return None
```

This function takes an integer `n` as an argument and returns the n-th Fibonacci number, checking whether it's prime. The function first checks if `n` is less than or equal to 1 and returns `n` if the condition is met. The function then calculates the n-th Fibonacci number using the formula `fib_n = math.sqrt(2) * math.sqrt(3)` and then checks if the Fibonacci number is prime using the `is_prime` function from the `pytagan` library.