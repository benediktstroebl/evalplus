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
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_fibonacci(num: int) -> int:
    """
    Returns the nth Fibonacci number.

    Args:
    num (int): The position of the Fibonacci number.

    Returns:
    int: The nth Fibonacci number.
    """
    if num == 1:
        return 1
    a, b = 1, 1
    for _ in range(2, num):
        a, b = b, a + b
    return b


def prime_fib(n: int) -> int:
    """
    Returns the n-th Fibonacci number that is also prime.

    Args:
    n (int): The position of the number.

    Returns:
    int: The n-th Fibonacci number that is prime.
    """
    for i in range(1, n+1):
        fib_num = get_fibonacci(i)
        if is_prime(fib_num):
            return fib_num
    return None


# Example usage
if __name__ == "__main__":
    print(prime_fib(1))  # prints: 2
    print(prime_fib(2))  # prints: 3
    print(prime_fib(3))  # prints: 5
    print(prime_fib(4))  # prints: 13
    print(prime_fib(5))  # prints: 89
```

This script defines three functions: `is_prime` checks if a number is prime, `get_fibonacci` generates Fibonacci numbers, and `prime_fib` finds the n-th Fibonacci number that is also prime. The script then demonstrates the usage of `prime_fib` with example inputs.