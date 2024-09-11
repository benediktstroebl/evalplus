```python
def is_prime(n: int) -> bool:
    """
    is_prime checks if a number is prime.

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
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def fibonacci() -> list:
    """
    fibonacci generates Fibonacci numbers on the fly.

    Yields:
    int: The next Fibonacci number.
    """
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci number to find.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    fib_generator = fibonacci()
    count = 0
    for num in fib_generator:
        if is_prime(num):
            count += 1
            if count == n:
                return num


# Example usage:
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

This script first checks if a number is prime with the `is_prime` function. It then generates Fibonacci numbers on the fly using the `fibonacci` generator function. The `prime_fib` function uses these two helper functions to find the n-th prime Fibonacci number. Finally, it demonstrates the usage of `prime_fib` with some examples.