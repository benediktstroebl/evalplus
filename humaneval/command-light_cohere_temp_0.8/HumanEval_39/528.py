```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    if n <= 3:
        return 2
    if n % 2 == 0:
        return 3
    prime = 4
    for i in range(5, n + 1, 2):
        if math.isprime(prime) == True:
            prime += 1
    return prime
```