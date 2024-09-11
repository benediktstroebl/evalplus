### Prime Fibonacci Numbers
#### A Python Script to Generate Prime Fibonacci Numbers

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
    Returns the nth prime Fibonacci number.

    Args:
    n (int): The position of the prime Fibonacci number.

    Returns:
    int: The nth prime Fibonacci number.
    """
    count = 0
    num = 0
    while count < n:
        num = fibonacci(num)
        if is_prime(num):
            count += 1
    return num


# Example usage:
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script defines three functions: `is_prime`, `fibonacci`, and `prime_fib`. The `is_prime` function checks if a number is prime, `fibonacci` generates the nth Fibonacci number, and `prime_fib` returns the nth prime Fibonacci number.

The `prime_fib` function uses a while loop to generate Fibonacci numbers and check if they are prime. When it finds the nth prime Fibonacci number, it returns it. The example usage at the end demonstrates how to use the `prime_fib` function to generate the first few prime Fibonacci numbers.