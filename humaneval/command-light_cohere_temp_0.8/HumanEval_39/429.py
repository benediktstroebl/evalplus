```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    if n == 2:
        return 2
    is_prime = [True] * (n - 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i - 1]:
            continue
        else:
            is_prime[i] = False
    for i in range(2, n):
        if is_prime[i]:
            return i
    return n
```