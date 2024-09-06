```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    else:
        limit = int(math.sqrt(n)) + 1
        is_prime = [True] * (limit + 1)
        for i in range(4, limit, 2):
            if is_prime[i]:
                is_prime[i + 1] = False
        for i in is_prime:
            if i == 2 or i == 3:
                continue
            else:
                break
        return limit
```