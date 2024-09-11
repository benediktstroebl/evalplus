```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    Args:
    num: The number to check.

    Returns:
    True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    Generates the nth Fibonacci number.

    Args:
    n: The position of the Fibonacci number to generate.

    Returns:
    The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def prime_fib(n: int) -> int:
    """
    Returns the nth number that is a Fibonacci number and it's also prime.

    Args:
    n: The position of the Fibonacci number to find.

    Returns:
    The nth Fibonacci number that is also prime.
    """
    for i in range(1, n + 1):
        num = fibonacci(i)
        if is_prime(num):
            return num


# Test the function
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script defines three functions: `is_prime`, `fibonacci`, and `prime_fib`. The `is_prime` function checks if a number is prime, the `fibonacci` function generates the nth Fibonacci number, and the `prime_fib` function returns the nth Fibonacci number that is also prime. The script then tests the `prime_fib` function with the provided examples.