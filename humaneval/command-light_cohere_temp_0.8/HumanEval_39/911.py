```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        def helper(i):
            if i <= n and math.prime.isprime(i):
                return helper(i+1) + 1
            else:
                return helper(i-1) + 2
        return helper(0)

print(prime_fib(5))
```