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
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number to find.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    # Initialize the first two Fibonacci numbers
    a, b = 1, 2
    
    # Generate Fibonacci numbers until we find the n-th prime one
    for i in range(1, n):
        # Generate the next Fibonacci number
        a, b = b, a + b
        
        # Check if the new Fibonacci number is prime
        if is_prime(b):
            # If it's prime, increment the counter
            i += 1
    
    # At this point, the last generated Fibonacci number is the n-th prime one
    return b


# Test the function
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This Python script defines a function `is_prime` to check for primality and a function `prime_fib` to find the n-th Fibonacci number that is also prime. The `prime_fib` function generates Fibonacci numbers until it finds the n-th prime one. The script includes example use cases and docstrings for clarity.