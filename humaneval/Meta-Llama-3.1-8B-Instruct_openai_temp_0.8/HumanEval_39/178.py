**Fibonacci and Prime Numbers**
================================

Here's a Python function to find the n-th Fibonacci number that's also prime.

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
    Generates the n-th Fibonacci number.
    
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
    Returns the n-th Fibonacci number that's also prime.
    
    Args:
        n (int): The position of the Fibonacci number.
    
    Returns:
        int: The n-th Fibonacci number that's also prime.
    """
    fib_num = 1
    while True:
        fib_num = fibonacci(fib_num)
        if is_prime(fib_num):
            if fib_num == prime_fib(n - 1) and n!= 1:
                continue
            return fib_num


# Example usage
print(prime_fib(1))
print(prime_fib(2))
print(prime_fib(3))
print(prime_fib(4))
print(prime_fib(5))
```

This script defines three functions: `is_prime` checks if a number is prime; `fibonacci` generates the n-th Fibonacci number; and `prime_fib` returns the n-th Fibonacci number that's also prime. The example usage at the end demonstrates how to call these functions with different inputs.