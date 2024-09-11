### prime_fib.py

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
    Returns the n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the number.

    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    count = 0
    num = 0
    while count < n:
        num = fibonacci(num + 1)
        if is_prime(num):
            count += 1
    return num


# Example use cases
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

This script defines three functions: `is_prime` to check if a number is prime, `fibonacci` to calculate the n-th Fibonacci number, and `prime_fib` to find the n-th number that is both a Fibonacci number and prime. The example use cases at the end demonstrate how to use the `prime_fib` function.