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


def is_perfect_square(num: int) -> bool:
    """
    Checks if a number is a perfect square.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is a perfect square, False otherwise.
    """
    root = num ** 0.5
    return int(root + 0.5) ** 2 == num


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the number to return.

    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    count = 0
    a, b = 1, 1
    while True:
        # Generate Fibonacci number
        a, b = b, a + b
        
        # Check if the Fibonacci number is prime
        if is_prime(b):
            count += 1
            if count == n:
                return b


# Test cases
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script defines three functions: `is_prime`, `is_perfect_square`, and `prime_fib`. The `is_prime` function checks if a number is prime, the `is_perfect_square` function checks if a number is a perfect square, and the `prime_fib` function returns the n-th number that is a Fibonacci number and it's also prime. The `prime_fib` function uses a loop to generate Fibonacci numbers and check if they are prime until it finds the n-th one.