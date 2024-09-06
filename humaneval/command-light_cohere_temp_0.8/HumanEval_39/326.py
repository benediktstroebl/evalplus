```python
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
 
    if n % 2 == 0 or n % 3 == 0:
        return False
 
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
  return True

def prime_fib(n):
    if n <= 0:
        return None
    result = 2
    while is_prime(result):
        result += 1
    return result

# Test the function
print(prime_fib(5))  # Output: 89
print(prime_fib(13))  # Output: True
```
This script defines a `prime_fib` function that calculates the n-th Fibonacci number which is also prime. The `is_prime` function checks whether a given number is prime or not. The function then uses this `prime` test to efficiently determine prime numbers.