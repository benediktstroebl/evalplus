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
    Returns the n-th Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number.

    Returns:
        int: The n-th Fibonacci number.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def prime_fib(n: int) -> int:
    """
    Returns the n-th Fibonacci number that is also prime.

    Args:
        n (int): The index of the prime Fibonacci number.

    Returns:
        int: The n-th prime Fibonacci number.
    """
    count = 0
    num = 0
    while count < n:
        num = fibonacci(num)
        if is_prime(num):
            count += 1
    return num


# Test cases
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script consists of three functions: `is_prime`, `fibonacci`, and `prime_fib`. The `is_prime` function checks if a number is prime by iterating from 2 to the square root of the number. The `fibonacci` function generates Fibonacci numbers iteratively. The `prime_fib` function uses these two functions to find the n-th Fibonacci number that is also prime. The test cases are included at the end of the script to verify the correctness of the `prime_fib` function.