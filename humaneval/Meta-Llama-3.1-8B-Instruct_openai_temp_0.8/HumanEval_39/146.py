### Prime Fibonacci Numbers
#### A Python Script to Find the n-th Prime Fibonacci Number

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
    for i in range(2, int(num**0.5) + 1):
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
    x = 0
    y = 1
    while y < num:
        z = x + y
        x = y
        y = z
    return y == num


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the number in the sequence.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    count = 0
    num = 1
    while True:
        num += 1
        if is_fibonacci(num) and is_prime(num):
            count += 1
            if count == n:
                return num


# Example usage
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script defines three functions: `is_prime`, `is_fibonacci`, and `prime_fib`. The `is_prime` function checks if a number is prime, the `is_fibonacci` function checks if a number is a Fibonacci number, and the `prime_fib` function finds the n-th prime Fibonacci number. The `prime_fib` function uses a simple iterative approach to generate Fibonacci numbers and check if they are prime.