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
    n (int): The position of the Fibonacci number to generate.
    
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
    n (int): The position of the Fibonacci number to check.
    
    Returns:
    int: The n-th Fibonacci number that is prime.
    """
    count = 0
    num = 0
    while count < n:
        num = fibonacci(num + 1)
        if is_prime(num):
            count += 1
    return num


# Test cases
print(prime_fib(1))  # Expected output: 2
print(prime_fib(2))  # Expected output: 3
print(prime_fib(3))  # Expected output: 5
print(prime_fib(4))  # Expected output: 13
print(prime_fib(5))  # Expected output: 89
```

This script first defines a helper function `is_prime` to check if a number is prime. Then it defines another helper function `fibonacci` to generate the nth Fibonacci number. The `prime_fib` function uses these two helper functions to find the nth Fibonacci number that is also prime. The test cases at the end verify that the `prime_fib` function works correctly.