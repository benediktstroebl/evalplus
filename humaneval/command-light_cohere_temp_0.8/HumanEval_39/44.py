```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    elif n <= 3:
        return 2
    else:
        m = n // 2
        if math.isumInt(m) and n % 2 == 0:
            return m + prime_fib(n % 2)
        else:
            return prime_fib(m) + prime_fib(n % 2)
``` 
This function uses the same approach as the original function, but it's a more efficient solution.  It checks divisibility of the number by the number itself and its other half and returns the result accordingly.