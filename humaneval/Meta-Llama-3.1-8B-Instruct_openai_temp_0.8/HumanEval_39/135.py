```python
def is_prime(n: int) -> bool:
    """
    Helper function to check if a number is prime.
    
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
    prime_fib returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number to check.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    a, b = 0, 1
    count = 0
    while True:
        # Check if the Fibonacci number is prime
        if is_prime(b):
            count += 1
            # Return the n-th prime Fibonacci number
            if count == n:
                return b
        # Generate the next Fibonacci number
        a, b = b, a + b


# Test the function
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script defines a helper function `is_prime` to check if a number is prime, and the main function `prime_fib` to find the n-th Fibonacci number that is also prime. The Fibonacci sequence is generated iteratively, and the `is_prime` function is used to check each number. The first n Fibonacci numbers that are prime are tracked, and the n-th one is returned.