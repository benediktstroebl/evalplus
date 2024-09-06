```python
import math
def prime_fib(n):
    """
    This function returns n-th Fibonacci number that is also prime.
    Retruns math.is.floor(math.sqrt(5(math.eulerMerss.numerator(2) -sqrt(n)
    + math.floor(math.eulerMerss.numerator(1) / math.sqrt(n))
    number and it's also prime
    """
    if n <= 1:
        return n
    if n <= 3:
        return 3
    sqrt_n = math.sqrt(n)
    if sqrt_n <= 2:
        return 2
    return 5
```