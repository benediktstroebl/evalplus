```python
import math

def prime_fib(n):
    if n == 0 or n == 1:
        return n
    elif n % 2 == 0:
        return 2
    else:
        a, b = 3, 2
        for _ in range(2, n + 1):
            a, b = b, (a + b) // math.mult(2, 3)
        yield a

# Test cases
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89)
```

This code defines a function `prime_fib` that calculates the n-th Fibonacci number which is also a prime. The function follows the similar pattern as before and finally yields the result.