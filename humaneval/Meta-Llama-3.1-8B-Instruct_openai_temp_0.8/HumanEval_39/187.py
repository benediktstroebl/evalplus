### Fibonacci and Prime Numbers
#### A Python Script to Find nth Number that is Both a Fibonacci and Prime Number

Below is a Python script that uses two helper functions to check if a number is prime and if it's a Fibonacci number.

```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    Args:
    num (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_perfect_square(x: int) -> bool:
    """
    Checks if a number is a perfect square.

    Args:
    x (int): The number to check.

    Returns:
    bool: True if the number is a perfect square, False otherwise.
    """
    s = int(x ** 0.5)
    return s * s == x


def is_fibonacci(n: int) -> bool:
    """
    Checks if a number is a Fibonacci number.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is a Fibonacci number, False otherwise.
    """
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


def prime_fib(n: int):
    """
    Returns nth number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the number.

    Returns:
    int: The nth number that is both a Fibonacci and prime number.
    """
    count = 0
    num = 1
    while True:
        if is_prime(num) and is_fibonacci(num):
            count += 1
            if count == n:
                return num
        num += 1


# Example usage:
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script defines the `is_prime`, `is_perfect_square`, `is_fibonacci` helper functions to check for primality, perfect squares, and Fibonacci numbers respectively. The `prime_fib` function uses a loop to find the nth number that is both a Fibonacci and prime number. The example usage at the end demonstrates how to use the `prime_fib` function.