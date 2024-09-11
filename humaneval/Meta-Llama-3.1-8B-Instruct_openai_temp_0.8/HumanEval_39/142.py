### Prime Fibonacci Sequence Generator
#### Python Script

```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    Args:
        num (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
        n (int): The position of the Fibonacci number to find.

    Returns:
        int: The n-th prime Fibonacci number.
    """
    a, b = 0, 1
    prime_count = 0
    while prime_count < n:
        a, b = b, a + b
        if is_prime(b):
            prime_count += 1
            if prime_count == n:
                return b
    return None


# Example usage
if __name__ == "__main__":
    print(prime_fib(1))   # Output: 2
    print(prime_fib(2))   # Output: 3
    print(prime_fib(3))   # Output: 5
    print(prime_fib(4))   # Output: 13
    print(prime_fib(5))   # Output: 89
```

This script first checks if a number is prime using the `is_prime` function, and then uses the `prime_fib` function to generate the n-th prime Fibonacci number. The Fibonacci sequence is generated on the fly, and the `is_prime` function is used to check if each generated number is prime. The script includes example usage at the end.