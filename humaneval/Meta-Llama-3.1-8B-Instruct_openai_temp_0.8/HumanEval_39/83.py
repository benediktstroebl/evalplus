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
    n (int): The position of the Fibonacci number to return.
    
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
    Returns the nth number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the number to return.
    
    Returns:
    int: The nth number that is a Fibonacci number and it's also prime.
    """
    count = 0
    num = 0
    i = 0
    while count < n:
        num = fibonacci(i)
        if is_prime(num):
            count += 1
        i += 1
    return num


# Test the function
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script defines three functions: `is_prime` checks if a number is prime, `fibonacci` returns the nth Fibonacci number, and `prime_fib` returns the nth number that is a Fibonacci number and it's also prime. The `prime_fib` function uses the `fibonacci` function to generate Fibonacci numbers and the `is_prime` function to check if they are prime. The test at the end checks that the `prime_fib` function works correctly for the examples provided in your prompt.