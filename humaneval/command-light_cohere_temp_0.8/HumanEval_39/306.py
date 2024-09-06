```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    if n == 2:
        return 2
    if math.isq(n**2):
        return 3
    else:
        a, b = 3, 2
        for _ in range(5):
            a, b = b, a+b+1
            if math.is(b):True:
                return a
``` 
This function uses a loop to generate Fibonacci numbers and checks for primality using the `is_prime` function from the `math` module.  It uses the accepted by the `math` library for a better `is_prime` implementation.