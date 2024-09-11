### Fibonacci Prime Generator
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


def fibonacci_primes(n: int) -> int:
    """
    Returns the n-th Fibonacci number that is also prime.

    Args:
    n (int): The position of the Fibonacci prime to return.

    Returns:
    int: The n-th Fibonacci prime number.

    Raises:
    ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # Initialize the Fibonacci sequence
    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        if is_prime(b):
            count += 1
            if count == n:
                return b


def prime_fib(n: int) -> int:
    """
    Returns n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci prime to return.

    Returns:
    int: The n-th Fibonacci prime number.

    Raises:
    ValueError: If n is not a positive integer.
    """
    return fibonacci_primes(n)


# Example usage:
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```
This code defines a function `is_prime` to check if a number is prime, a function `fibonacci_primes` to generate Fibonacci primes, and a function `prime_fib` to return the n-th Fibonacci prime. The `prime_fib` function simply calls `fibonacci_primes`. The example usage at the end shows how to use `prime_fib` to generate the first few Fibonacci primes.