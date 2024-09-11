### Fibonacci Prime Numbers

This Python script generates the `n`-th number that is a Fibonacci number and it's also prime.

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


def fibonacci_prime(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci prime number.

    Returns:
    int: The n-th Fibonacci prime number.
    """
    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a + b
        if is_prime(b):
            count += 1
            if count == n:
                return b
    return None


def prime_fib(n: int):
    """
    Alias for fibonacci_prime.

    Args:
    n (int): The position of the Fibonacci prime number.

    Returns:
    int: The n-th Fibonacci prime number.
    """
    return fibonacci_prime(n)


# Example usage:
if __name__ == "__main__":
    print(prime_fib(1))  # 2
    print(prime_fib(2))  # 3
    print(prime_fib(3))  # 5
    print(prime_fib(4))  # 13
    print(prime_fib(5))  # 89
```

This script defines two helper functions: `is_prime` to check if a number is prime and `fibonacci_prime` to generate the `n`-th Fibonacci prime number. It uses an iterative approach to generate Fibonacci numbers and checks each one for primality using the `is_prime` function. The `prime_fib` function is an alias for `fibonacci_prime` and is the main entry point for the functionality.