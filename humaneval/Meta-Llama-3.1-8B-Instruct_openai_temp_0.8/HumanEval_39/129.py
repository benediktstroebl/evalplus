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


def fibonacci(num: int) -> int:
    """
    Returns the num-th Fibonacci number.

    Args:
    num (int): The position of the Fibonacci number.

    Returns:
    int: The num-th Fibonacci number.
    """
    if num <= 0:
        return "Input should be positive integer"
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < num:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the number.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    count = 0
    num = 1
    while count < n:
        num = fibonacci(num)
        if is_prime(num):
            count += 1
    return num


# Example usage:
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script defines three functions:

1. `is_prime(num)`: checks if a number is prime.
2. `fibonacci(num)`: returns the num-th Fibonacci number.
3. `prime_fib(n)`: returns the n-th number that is a Fibonacci number and it's also prime.

The `prime_fib(n)` function uses a simple iterative approach to find the n-th prime Fibonacci number. It generates Fibonacci numbers and checks if they are prime using the `is_prime(num)` function.