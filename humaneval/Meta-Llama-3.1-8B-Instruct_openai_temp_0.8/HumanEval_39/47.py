### Prime Fibonacci Number Generator
#### A Python script to generate the n-th prime Fibonacci number

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
    Generates the n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to generate.

    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci number to generate.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    count = 0
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num
        i += 1


# Example usage
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"Prime Fibonacci number at position {i}: {prime_fib(i)}")
```

This script first defines helper functions to check if a number is prime and to generate Fibonacci numbers. The `prime_fib` function uses these helpers to generate the n-th prime Fibonacci number. The example usage at the end demonstrates how to use the `prime_fib` function to generate the first 5 prime Fibonacci numbers.