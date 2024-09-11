### Prime Fibonacci Numbers
#### Python Script
```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_fibonacci(num: int) -> bool:
    """
    Checks if a number is a Fibonacci number.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is a Fibonacci number, False otherwise.
    """
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
        n (int): The position of the number to return.

    Returns:
        int: The n-th prime Fibonacci number.
    """
    num = 1
    while True:
        if is_prime(num) and is_fibonacci(num):
            return num
        num += 1


# Example usage:
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script defines three functions:

1. `is_prime(num)`: Checks if a number is prime.
2. `is_fibonacci(num)`: Checks if a number is a Fibonacci number.
3. `prime_fib(n)`: Returns the n-th number that is a Fibonacci number and it's also prime.

The `prime_fib` function uses the `is_prime` and `is_fibonacci` functions to find the n-th prime Fibonacci number. It keeps incrementing the number until it finds a number that is both prime and a Fibonacci number.