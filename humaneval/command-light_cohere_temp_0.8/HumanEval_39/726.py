```python
import math
def prime_fib(n):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n - 2)
    else:
        limit = int(math.sqrt(n) * 2)
        for i in range(3, limit + 1, 2):
            if math.isprime(i):
                return i
        else:
            return prime_fib(n - i)
``` 
This function uses a backtracking algorithm to find the n-th Fibonacci number that is prime, and tests its correctness with the `math.isprime()` function.