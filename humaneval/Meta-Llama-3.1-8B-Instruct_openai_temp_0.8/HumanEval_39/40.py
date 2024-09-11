### Prime Fibonacci Sequence Generator
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


def fibonacci(n: int) -> int:
    """
    Generates the n-th Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number to generate.

    Returns:
        int: The n-th Fibonacci number.
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
        n (int): The index of the prime Fibonacci number to return.

    Returns:
        int: The n-th prime Fibonacci number.
    """
    count = 0
    num = 1
    while True:
        fib_num = fibonacci(num)
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num
        num += 1


# Example usage:
print(prime_fib(1))   # 2
print(prime_fib(2))   # 3
print(prime_fib(3))   # 5
print(prime_fib(4))   # 13
print(prime_fib(5))   # 89
```
This script defines three functions: `is_prime`, `fibonacci`, and `prime_fib`. The `is_prime` function checks if a number is prime, the `fibonacci` function generates the n-th Fibonacci number, and the `prime_fib` function returns the n-th number that is a Fibonacci number and it's also prime. The example usage at the end demonstrates how to use the `prime_fib` function to generate the first five prime Fibonacci numbers.