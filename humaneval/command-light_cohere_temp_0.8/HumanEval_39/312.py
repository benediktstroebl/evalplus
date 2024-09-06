```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    else:
        prime = 2
        for i in range(2, n + 1):
            is_prime = True
            d = i
            while d <= 1000000 and math.isprime(d):
                is_prime = False
                d += 1
            if is_prime:
                prime = d
        return prime
```