```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n <= 1:
        return n
    num, num2 = 2, 3
    for _ in range(2, n):
        if math.isprime(num):
            num2 = num
        else:
            break
    if num2 == 3:
        return num
    else:
        return math.isqio(n)
```