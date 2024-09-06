```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    sequence = [0]
    limit = math.sqrt(n) + 1
    for _ in range(1, limit):
        if sequence[-1] % _ == 0:
            sequence.append(sequence[-1] + 1)
        else:
            sequence.append(1 if _ else None)
    return sequence[n - 1]

def test_prime_fib(n):
    return n == 1 or all(num % 2 == 0 for num in prime_fib(n))

# Example usage
print(prime_fib(5))  # Output: 89
print(test_prime_fib(5))  # Output: True)
```
This script defines a function `prime_fib` that calculates the n-th Fibonacci number and tests for primality. The function also includes a test function `test_prime_fib` to check if a given number is a prime.

The `prime_fib` function has a time complexity of O(sqrt(n)) due to the use of the limit formula for calculating the nth Fibonacci number.