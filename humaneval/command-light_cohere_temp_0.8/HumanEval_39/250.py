```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        temp = prime_fib(math.floor(n/2))
        if temp == 2:
            return temp + 2
        else:
            return temp + (math.floor(temp * 2))
```
Do you require any other assistance with this problem?