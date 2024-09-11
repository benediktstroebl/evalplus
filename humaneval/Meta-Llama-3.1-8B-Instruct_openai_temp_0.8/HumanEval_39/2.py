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
    Returns the nth Fibonacci number.

    Args:
    n (int): The index of the Fibonacci number.

    Returns:
    int: The nth Fibonacci number.
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
    n (int): The index of the Fibonacci number.

    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    i = 1
    while True:
        fib = fibonacci(i)
        if is_prime(fib):
            return fib
        i += 1


# Test cases
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

This script defines three functions: `is_prime`, `fibonacci`, and `prime_fib`. The `is_prime` function checks if a number is prime, the `fibonacci` function returns the nth Fibonacci number using recursion, and the `prime_fib` function returns the n-th number that is a Fibonacci number and it's also prime by iterating over Fibonacci numbers and checking if they are prime.

The script then tests the `prime_fib` function with the test cases provided.