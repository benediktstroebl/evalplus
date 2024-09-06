```python
import math
def prime_fib(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    if n == 1:
        return 2
    else:
        temp = prime_fib(n // 2)
        if temp == 2:
            return temp + 2
        elif temp == 3:
            return temp
        else:
            i = 4
            while i <= n:
                if math.isq(prime_fib(i), temp) == True:
                    return i + temp
                i += 2
            else:
                return i + temp + 2
```