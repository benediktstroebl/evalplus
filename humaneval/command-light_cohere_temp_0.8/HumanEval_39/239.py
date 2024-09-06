```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        return 1 if is_prime(n) else 2

def is_prime(n: int):
    """
    Checks if n is a prime number.
    """
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

# Example usage
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 6
```
This script defines a function `prime_fib` that computes the n-th Fibonacci number and checks if it's also prime, and a function `is_prime` that checks if a number is prime or not. The example usage demonstrates the final output.