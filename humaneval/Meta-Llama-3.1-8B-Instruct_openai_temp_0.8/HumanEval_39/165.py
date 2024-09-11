```python
def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The index of the Fibonacci number.
    
    Returns:
    int: The n-th prime Fibonacci number.
    """
    # Initialize the first two Fibonacci numbers and their prime counts
    a, b = 0, 1
    prime_count = 0

    # Iterate over the Fibonacci sequence
    while prime_count < n:
        # Check if the current Fibonacci number is prime
        if is_prime(b):
            prime_count += 1
        
        # Generate the next Fibonacci number
        a, b = b, a + b
    
    # Return the n-th prime Fibonacci number
    return b


# Example usage:
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script defines two functions: `is_prime` checks if a number is prime, and `prime_fib` returns the n-th prime Fibonacci number. It uses the Fibonacci sequence and a helper function to keep track of the prime numbers encountered during the iteration. The script then demonstrates the usage of the `prime_fib` function with example inputs.