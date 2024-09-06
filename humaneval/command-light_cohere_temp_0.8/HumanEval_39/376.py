```python
import math

def prime_fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    prime_fib_prime = [True] * (math.max + 1)
    prime_fib_prime[-1] = False
    for num in prime_fib_prime:
        if num <= n:
            break
        if num == 2:
            prime_fib_prime[num] = False
        else:
            prime_fib_prime[num] = True
               
    for num in range(2, n + 1):
        if prime_fib_prime[num]:
            return num
    return None
```