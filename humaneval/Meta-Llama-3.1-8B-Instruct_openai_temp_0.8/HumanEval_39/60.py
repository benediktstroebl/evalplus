### Fibonacci Prime Generator

Below is a Python script that generates the nth number in the Fibonacci sequence that is also a prime number.

```python
import math

def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(5, sqrt_n + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def fibonacci_prime(n: int) -> int:
    """
    Returns the nth number in the Fibonacci sequence that is also a prime number.

    Args:
        n (int): The position of the Fibonacci number.

    Returns:
        int: The nth Fibonacci prime number.
    """
    a, b = 0, 1
    prime_count = 0
    while prime_count < n:
        if is_prime(b):
            prime_count += 1
            if prime_count == n:
                return b
        a, b = b, a + b
    return None


if __name__ == "__main__":
    print(fibonacci_prime(1))  # Output: 2
    print(fibonacci_prime(2))  # Output: 3
    print(fibonacci_prime(3))  # Output: 5
    print(fibonacci_prime(4))  # Output: 13
    print(fibonacci_prime(5))  # Output: 89
```

This script first defines a helper function `is_prime` to check if a number is prime. It then uses this function in `fibonacci_prime` to generate the nth Fibonacci prime number. The script uses an iterative approach to build up the Fibonacci sequence and checks each number for primality. When the nth prime is found, it is returned.