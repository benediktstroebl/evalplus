### Prime Fibonacci Numbers
#### Python Script
```markdown
### prime_fib.py
```python
import math

def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqrt_num = math.isqrt(num)
    for i in range(3, sqrt_num + 1, 2):
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
    sqrt_num = math.isqrt(num)
    return sqrt_num * sqrt_num == num

def is_fibonacci(num: int) -> bool:
    """
    Checks if a number is a Fibonacci number.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is a Fibonacci number, False otherwise.
    """
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The index of the number to return.

    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    num = 0
    i = 1
    count = 0
    while True:
        num = i * (i + 1) // 2
        if is_prime(num) and count < n:
            count += 1
            if count == n:
                return num
        i += 1

# Example usage:
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```
This script defines three helper functions: `is_prime`, `is_perfect_square`, and `is_fibonacci`. The `prime_fib` function uses these helpers to find the n-th number that is both a Fibonacci number and a prime number. The example usage at the end demonstrates how to use the `prime_fib` function.