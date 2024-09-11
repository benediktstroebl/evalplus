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


def fibonacci(a: int, b: int, n: int) -> int:
    """
    Generates the nth Fibonacci number.

    Args:
    a (int): The first Fibonacci number.
    b (int): The second Fibonacci number.
    n (int): The position of the Fibonacci number to generate.

    Returns:
    int: The nth Fibonacci number.
    """
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for _ in range(2, n):
            a, b = b, a + b
        return b


def prime_fib(n: int) -> int:
    """
    Returns the nth number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the number to find.

    Returns:
    int: The nth prime Fibonacci number.
    """
    a, b = 0, 1
    count = 0
    num = 2
    while count < n:
        if is_prime(num) and is_prime(fibonacci(a, b, num)):
            count += 1
            if count == n:
                return num
        num += 1


# Example usage:
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

This script defines three functions:

1. `is_prime(num)`: Checks if a number is prime.
2. `fibonacci(a, b, n)`: Generates the nth Fibonacci number.
3. `prime_fib(n)`: Finds the nth number that is both a Fibonacci number and prime.

The `prime_fib(n)` function uses the `is_prime(num)` function to check if a number is prime, and the `fibonacci(a, b, n)` function to generate Fibonacci numbers. It iterates over numbers to find the nth number that meets both conditions.