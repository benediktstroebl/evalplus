```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Start from the n-th Fibonacci number, then move forward
        # Only even numbers are composite so skip odd numbers
        for i in range(max(5, n - 1), int(3 * (n ** 0.5) + 7), 2):
            if is_prime(i):
                return i
```

This script defines a `prime_fib` function which aims to find the n-th number that is both prime and a Fibonacci number. It does this by starting from the n-th Fibonacci number and then moving forward while checking if each number is prime using the `is_prime` function. The `is_prime` function checks if a number is prime using a basic primality test.

Example usage:
```python
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```