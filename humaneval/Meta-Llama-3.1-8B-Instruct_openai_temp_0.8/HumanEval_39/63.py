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


def nth_prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the number in the sequence.

    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    a, b = 0, 1
    prime_count = 0
    while True:
        # Check if the current Fibonacci number is prime
        if is_prime(b):
            prime_count += 1
            # If it's the n-th prime Fibonacci number, return it
            if prime_count == n:
                return b
        # Generate the next Fibonacci number
        a, b = b, a + b


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the number in the sequence.

    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    return nth_prime_fib(n)


# Test cases
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

This script uses two helper functions: `is_prime` to check if a number is prime, and `nth_prime_fib` to generate the n-th number that is a Fibonacci number and it's also prime. The `prime_fib` function is a simple wrapper around `nth_prime_fib`. The script includes test cases at the end to verify that the functions work correctly.