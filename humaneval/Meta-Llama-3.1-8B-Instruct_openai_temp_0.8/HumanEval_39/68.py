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
    n (int): The position of the Fibonacci number.

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
    n (int): The position of the Fibonacci number.

    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    count = 0
    num = 0
    while True:
        num = fibonacci(count)
        if is_prime(num):
            if count == n:
                return num
            count += 1
        else:
            count += 1

# Example usage
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

This script defines three functions: `is_prime` checks if a number is prime, `fibonacci` generates the nth Fibonacci number, and `prime_fib` returns the n-th number that is a Fibonacci number and it's also prime. It then demonstrates the usage of the `prime_fib` function by printing the first five numbers that are Fibonacci numbers and prime.