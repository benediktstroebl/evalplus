```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    Args:
    num (int): Number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_fibonacci(num: int) -> bool:
    """
    Checks if a number is a Fibonacci number.

    Args:
    num (int): Number to check.

    Returns:
    bool: True if the number is a Fibonacci number, False otherwise.
    """
    x = 0
    y = 1
    while y < num:
        z = x + y
        x = y
        y = z
    return y == num


def prime_fib(n: int) -> int:
    """
    Returns n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): Index of the number to find.

    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    num = 0
    index = 1
    while index <= n:
        num += 1
        if is_prime(num) and is_fibonacci(num):
            index += 1
    return num


# Example usage:
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

This script defines two helper functions `is_prime` and `is_fibonacci` to check if a number is prime and a Fibonacci number, respectively. The `prime_fib` function generates Fibonacci numbers and checks if they are prime, returning the `n-th` number that meets this condition. The example usage demonstrates how to use the `prime_fib` function to find the `n-th` prime Fibonacci number.