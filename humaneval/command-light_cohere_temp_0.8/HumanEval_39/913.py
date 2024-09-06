```python
import math
def prime_fib(n):
    if n == 0:
        return 1
    if n < 2:
        return 0
    if n % 2 == 0:
        return prime_fib(n-1) + prime_fib(n-2)
    else:
        sqrt_ = math.sqrt(n)
        prime_fib = math.sqrt(2) * ((sqrt_ * sqrt_ - 1) / sqrt_ - 1) ** 2
        for i in range(3, int(sqrt_ + 1), 2):
            if n >= i * i:
                break
        return prime_fib
```