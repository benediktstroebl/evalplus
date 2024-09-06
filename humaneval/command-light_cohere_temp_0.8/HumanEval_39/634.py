```python
import math
def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and is also prime.
    It uses some formula from http://math.st.gense.probability.
    
    >>> prime_
    saw:
    -1
    2
    ^= 3
    5
    ^= 13
    13
    ^= 89
    89
    ^= n+1

    If n is even, return the square of the above number
    If n is odd, return sqrt(n^2 - 1) + 1
    """
    if n % 2 == 0:
        return pow(2, n)
    else:
        return math.sqrt(math.sqrt(n**2 - -d**2 -1) + 1
```