### Fibonacci Prime Generator

The following Python script generates the `n-th` number that is both a Fibonacci number and a prime number.

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
    Generates Fibonacci numbers.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci prime.

    Returns:
    int: The n-th Fibonacci prime.
    """
    fib_gen = fibonacci()
    count = 0
    num = 0
    while count < n:
        num = next(fib_gen)
        if is_prime(num):
            count += 1
    return num


# Example usage
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

This script defines three functions: `is_prime` checks if a number is prime, `fibonacci` generates Fibonacci numbers, and `prime_fib` returns the `n-th` Fibonacci number that is also prime. The example usage at the end demonstrates how to use `prime_fib` with the first five values of `n`.