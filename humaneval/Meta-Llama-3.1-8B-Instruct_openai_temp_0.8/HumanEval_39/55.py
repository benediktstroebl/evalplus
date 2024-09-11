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
    n (int): The position of the Fibonacci number to return.
    
    Returns:
    int: The n-th Fibonacci number.
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
    Returns the n-th Fibonacci number that is also prime.
    
    Args:
    n (int): The position of the Fibonacci number to return.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    count = 0
    num = 1
    while count < n:
        fib_num = fibonacci(num)
        if is_prime(fib_num):
            count += 1
            result = fib_num
        num += 1
    return result


# Example use cases:
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script defines three functions:

1. `is_prime(num)`: Checks if a number is prime.
2. `fibonacci(n)`: Returns the n-th Fibonacci number.
3. `prime_fib(n)`: Returns the n-th Fibonacci number that is also prime.

The `prime_fib(n)` function uses the `fibonacci(n)` function to generate Fibonacci numbers and the `is_prime(num)` function to check if each Fibonacci number is prime. It keeps track of the count of prime Fibonacci numbers found and returns the n-th prime Fibonacci number.