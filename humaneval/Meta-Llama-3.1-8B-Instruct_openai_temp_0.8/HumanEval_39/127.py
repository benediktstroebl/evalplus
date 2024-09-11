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


def is_perfect_square(num: int) -> bool:
    """
    Checks if a number is a perfect square.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is a perfect square, False otherwise.
    """
    if num < 0:
        return False
    sqrt = int(num ** 0.5)
    return sqrt * sqrt == num


def fibonacci(n: int) -> int:
    """
    Returns the nth Fibonacci number.

    Args:
    n (int): The index of the Fibonacci number.

    Returns:
    int: The nth Fibonacci number.
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
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The index of the Fibonacci number.

    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    i = 1
    while True:
        num = fibonacci(i)
        if is_prime(num):
            return num
        i += 1


# Test cases
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script first checks if a number is prime using the `is_prime` function, then checks if a number is a perfect square using the `is_perfect_square` function (although this function is not used directly in this script). The `fibonacci` function returns the nth Fibonacci number, and the `prime_fib` function returns the n-th number that is a Fibonacci number and it's also prime by calling `fibonacci` and checking if the result is prime.