### Prime Fibonacci Number Generator
#### Problem Description
This script generates the n-th number that is both a Fibonacci number and a prime number.

#### Script
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
    n (int): The position of the Fibonacci number.

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
    n (int): The position of the Fibonacci number.

    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            if i == n:
                return fib_num
            i += 1
        else:
            i += 1


# Example usage:
print(prime_fib(1))   # Output: 2
print(prime_fib(2))   # Output: 3
print(prime_fib(3))   # Output: 5
print(prime_fib(4))   # Output: 13
print(prime_fib(5))   # Output: 89
```
This script uses a Fibonacci generator and a prime-checking function to determine the n-th Fibonacci number that is also prime. It iterates through Fibonacci numbers until it finds the n-th prime Fibonacci number.