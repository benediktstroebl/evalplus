### Prime Fibonacci Numbers Generator

Below is a Python function that generates the n-th prime Fibonacci number. This function uses an iterative approach to generate Fibonacci numbers and a helper function to check for primality.

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


def fibonacci():
    """
    Generates Fibonacci numbers on the fly.

    Yields:
    int: The next Fibonacci number.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the number in the prime Fibonacci sequence.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    fib_gen = fibonacci()
    count = 0
    while True:
        num = next(fib_gen)
        if is_prime(num):
            count += 1
            if count == n:
                return num


# Example usage
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script uses a generator to produce Fibonacci numbers on the fly, which is more memory-efficient than storing the entire sequence in memory. The `is_prime` function checks if a number is prime, and the `prime_fib` function uses these helper functions to find the n-th prime Fibonacci number. The example usage at the end demonstrates how to use this function to generate prime Fibonacci numbers.