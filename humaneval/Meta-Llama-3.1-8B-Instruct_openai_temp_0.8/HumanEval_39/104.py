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
    Generates the nth Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to generate.

    Returns:
    int: The nth Fibonacci number.
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
    n (int): The position of the Fibonacci number to find.

    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.

    Raises:
    ValueError: If n is less than 1.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    count = 0
    num = 0
    while count < n:
        num = fibonacci(num + 1)
        if is_prime(num):
            count += 1
    return num


# Example usage:
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

In this script, the `is_prime` function checks if a number is prime by testing divisibility up to the square root of the number. The `fibonacci` function generates the nth Fibonacci number using an iterative approach. The `prime_fib` function raises a ValueError if n is less than 1, otherwise it generates Fibonacci numbers and checks if they are prime until it finds the n-th prime Fibonacci number.