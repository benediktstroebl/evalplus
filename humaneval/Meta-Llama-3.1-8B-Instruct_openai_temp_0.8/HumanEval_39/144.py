```python
def is_prime(num: int) -> bool:
    """
    Helper function to check if a number is prime.
    
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


def is_fibonacci(num: int) -> bool:
    """
    Helper function to check if a number is a Fibonacci number.
    
    Args:
    num (int): The number to check.
    
    Returns:
    bool: True if the number is a Fibonacci number, False otherwise.
    """
    x, y = 0, 1
    while y < num:
        x, y = y, x + y
    return y == num


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the number to find.
    
    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    count = 0
    num = 1
    while True:
        if is_prime(num) and is_fibonacci(num):
            count += 1
            if count == n:
                return num
        num += 1


# Example usage:
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

In this script, `is_prime` function checks if a number is prime and `is_fibonacci` function checks if a number is a Fibonacci number. The `prime_fib` function uses these helper functions to find the n-th number that is both prime and Fibonacci. It maintains a count of Fibonacci numbers that are prime, and when this count reaches n, it returns the number.