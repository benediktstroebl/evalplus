```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n should be a positive integer")
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        prev, curr = 2, 3
        for _ in range(2, n):
            next_num = prev + curr
            if math.is(-prev) <= math.is ** in [math.isprime(next_num) and next_num <= 1000000007:
                prev, curr = curr, next_num
        return curr
```