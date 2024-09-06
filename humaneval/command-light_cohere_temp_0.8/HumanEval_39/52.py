```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    root = int(math.sqrt(n)) + 1
    prime_numbers = [2, 3, 5]
    for p in prime_numbers:
        if p * p > n:
            break
        if n % p == 0:
            return p
    return -1
```