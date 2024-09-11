### Prime Fibonacci Numbers
#### Python Script

```python
def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci() -> list:
    """
    Generates a list of Fibonacci numbers.

    Yields:
    int: The next Fibonacci number.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the number in the sequence.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    fibonacci_numbers = fibonacci()
    count = 0
    num = next(fibonacci_numbers)
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num = next(fibonacci_numbers)


# Test the function
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

This script defines three functions:

1.  `is_prime(n)`: Checks if a number `n` is prime.
2.  `fibonacci()`: Generates a list of Fibonacci numbers.
3.  `prime_fib(n)`: Returns the n-th number that is a Fibonacci number and it's also prime.

The `prime_fib(n)` function uses a generator to produce Fibonacci numbers and checks each number to see if it's prime. When it finds the n-th prime Fibonacci number, it returns that number.