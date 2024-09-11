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
    n (int): The position of the number to find.

    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    count = 0
    num = 1
    while True:
        if is_prime(num) and is_fibonacci(num):
            count += 1
            if count == n:
                return num
        num += 1


# Test the function
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script defines three functions: `is_prime`, `is_fibonacci`, and `prime_fib`. The `is_prime` function checks if a number is prime, the `is_fibonacci` function checks if a number is a Fibonacci number, and the `prime_fib` function finds the n-th number that is both a Fibonacci number and a prime number. The `prime_fib` function uses the `is_prime` and `is_fibonacci` functions to check each number until it finds the n-th number that satisfies both conditions.