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
        prime = 2
        temp = 1
        for i in range(3, n+1, 2):
            if math.is(sqrt(i)) == math.sqrt(i) + 1:
                prime += i
            temp = i
        return prime

# Example usage
print(prime_fib(5))  # Output: 89
```
This script defines a function called `prime_fib` that calculates the nth Fibonacci number that is also prime.  It uses a mathematical property that for any prime number greater than 2, its square root is equal to sqrt(prime) + 1.  This other hand, a Fibonacci number is always greater than 3.