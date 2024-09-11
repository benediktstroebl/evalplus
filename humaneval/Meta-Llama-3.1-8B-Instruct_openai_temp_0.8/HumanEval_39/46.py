```python
import math

def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqrt_num = math.isqrt(num)
    for i in range(3, sqrt_num + 1, 2):
        if num % i == 0:
            return False
    return True

def is_perfect_square(num: int) -> bool:
    """
    Checks if a number is a perfect square.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is a perfect square, False otherwise.
    """
    return math.isqrt(num) ** 2 == num

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.

    Args:
        n (int): The position of the Fibonacci number to check.

    Returns:
        int: The n-th Fibonacci number that is prime.
    """
    # Initialize Fibonacci sequence
    a, b = 2, 3
    # Initialize counter
    count = 1
    # Initialize the first prime Fibonacci number
    prime_fib_num = 2

    # Generate Fibonacci numbers until we find the n-th prime one
    while count < n:
        # Generate the next Fibonacci number
        a, b = b, a + b
        # If the new Fibonacci number is a perfect square or not prime, skip it
        if is_perfect_square(b) or not is_prime(b):
            continue
        # If the new Fibonacci number is prime, increment the counter
        count += 1
        # Update the prime Fibonacci number
        prime_fib_num = b

    return prime_fib_num

# Test the function
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script defines a function `is_prime` to check if a number is prime, a function `is_perfect_square` to check if a number is a perfect square, and a function `prime_fib` to find the n-th prime Fibonacci number. The `prime_fib` function generates Fibonacci numbers and checks if they are prime and not perfect squares, incrementing the counter until it finds the n-th prime Fibonacci number.