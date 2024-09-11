```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.
    
    Args:
    num: The number to check for primality.
    
    Returns:
    True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    Generates the nth Fibonacci number.
    
    Args:
    n: The position of the Fibonacci number.
    
    Returns:
    The nth Fibonacci number.
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
    n: The position of the prime Fibonacci number.
    
    Returns:
    The nth prime Fibonacci number.
    """
    count = 0
    num = 1
    while True:
        if is_prime(fibonacci(num)):
            count += 1
            if count == n:
                return fibonacci(num)
        num += 1


# Example usage:
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script first defines a helper function `is_prime` to check if a number is prime, then a helper function `fibonacci` to generate the nth Fibonacci number. The main function `prime_fib` generates Fibonacci numbers and checks if they are prime, returning the nth prime Fibonacci number. The example usage at the end demonstrates how to use this function to find the nth prime Fibonacci number.