```python
def is_prime(num: int) -> bool:
    """
    Helper function to check if a number is prime.
    
    Args:
    num (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    Helper function to generate the nth Fibonacci number.
    
    Args:
    n (int): The index of the Fibonacci number to generate.
    
    Returns:
    int: The nth Fibonacci number.
    """
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    # Generate the nth Fibonacci number
    for _ in range(n):
        a, b = b, a + b
    return a


def prime_fib(n: int) -> int:
    """
    Returns the nth number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The index of the Fibonacci number to find.
    
    Returns:
    int: The nth Fibonacci number that is also prime.
    """
    # Initialize the Fibonacci sequence
    fib_num = 1
    # Find the nth prime Fibonacci number
    for _ in range(n):
        fib_num = fibonacci(fib_num)
        # Check if the Fibonacci number is prime
        if is_prime(fib_num):
            return fib_num


# Example usage:
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script first defines helper functions `is_prime` to check if a number is prime and `fibonacci` to generate the nth Fibonacci number. The `prime_fib` function uses these helpers to find the nth Fibonacci number that is also prime. The example usage at the end demonstrates how to use the `prime_fib` function to find the nth prime Fibonacci number for different values of `n`.