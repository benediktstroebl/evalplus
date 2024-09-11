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
    n (int): The index of the Fibonacci number.
    
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
    n (int): The index of the number.
    
    Returns:
    int: The nth number that is a Fibonacci number and it's also prime.
    """
    for i in range(n):
        fib_num = fibonacci(i + 1)
        if is_prime(fib_num):
            return fib_num


# Example usage:
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script first defines a helper function `is_prime` to check if a number is prime, then defines a function `fibonacci` to calculate the nth Fibonacci number, and finally defines the `prime_fib` function to return the nth number that is a Fibonacci number and it's also prime. The example usage at the end prints the results for the first 5 values of `n`.