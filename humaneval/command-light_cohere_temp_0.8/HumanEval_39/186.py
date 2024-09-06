```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    if n <= 3:
        return 2
    elif n % 2 == 0:
        return math.sqrt(5) + 1
    else:
        return math.sqrt(5) + math.sqrt(5)
```
This function calculates the n-th Fibonacci number that is prime, given n as an input.