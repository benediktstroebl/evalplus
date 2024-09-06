```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    elif n % 2 == 0:
        return prime_fib(n // 2) + 2
    else:
        return math.isq((n(prime_fib(n // 2) + 2) * (prime_fib(n // 3) + 2) ** 0.5) + 4)
```
This code defines a function `prime_fib` that computes and returns the n-th Fibonacci number which is prime. 

The function first checks if `n` is less than or equal to 1 and returns `n` directly. 

If `n` is 2, it returns `2`. 

If `n` is odd, it recursively calls `prime_fib(n // 2)` and adds 2. 

The function then computes the product of the two preceding Fibonacci numbers (which are prime) raised to the power of 0.5, and adds 4 to get the result.