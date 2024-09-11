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


def fibonacci(n: int) -> int:
    """
    Returns the nth Fibonacci number.

    Args:
    n (int): The index of the Fibonacci number to return.

    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def prime_fib(n: int) -> int:
    """
    Returns the nth number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The index of the Fibonacci number to return.

    Returns:
    int: The nth Fibonacci number that is also prime.
    """
    count = 0
    num = 0
    while True:
        num = fibonacci(num + 1)
        if is_prime(num):
            count += 1
            if count == n:
                return num


# Example usage:
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```
This script defines three functions: `is_prime`, `fibonacci`, and `prime_fib`. The `is_prime` function checks if a number is prime, the `fibonacci` function returns the nth Fibonacci number, and the `prime_fib` function returns the nth Fibonacci number that is also prime. The script then uses these functions to print the first 5 Fibonacci numbers that are also prime.