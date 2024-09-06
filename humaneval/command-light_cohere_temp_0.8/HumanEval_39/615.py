```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 2
    if n == 2:
        return 3
    series = [0]
    for i in range(3, n + 1):
        series.append(math.floor(math.sqrt((i +2 + series[-1])))
    for i in series:
        if i % 2 == 0:
            continue
        else:
            return i
```