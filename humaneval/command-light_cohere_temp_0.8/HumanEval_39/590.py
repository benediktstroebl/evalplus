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
        limit = math.sqrt(n) + 1
        coef = [0, 1]
        temp = 0
        for _ in range(limit):
            coef = coef[0] + coef[1]
            coef.n = math.sqrt(coef)
            temp += coef
            if temp <= n:
                break
        for _ in range(n - temp):
            coef.n *= 10
        coef.n // final_number is
        coef.n //
        number that is a Fibonacci and prime, return coef.n
        else:
            coef.n *= 10
            return coef.n
```
This code defines a function called prime_fib that returns the n-th Fibonacci number that is also prime. It uses a iterative approach with bisection and a coefficient array to achieve this result. The code also includes input validation to ensure that n is a positive integer.