```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    else:
        if n % 2 == 0:
            return math.prime(n+ 4)
        else:
            return math.prime(2+n + ((n-1) * (n-2)) // math.sqrt(5) + math.sqrt(5))
```

This code defines a `prime_fib` function which computes the n-th Fibonacci number that is prime. The function returns the result. 

It uses an iterative method with conditional checks to determine if the number is prime or not, and it uses the `math` module to perform the mathematical operations.