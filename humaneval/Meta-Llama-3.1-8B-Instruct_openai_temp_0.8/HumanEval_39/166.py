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
    Returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number.
    
    Returns:
    int: The n-th prime Fibonacci number.
    """
    a, b = 0, 1
    count = 0
    
    while True:
        # Check if the current Fibonacci number is prime
        if is_prime(b):
            count += 1
            # If it's the n-th prime Fibonacci number, return it
            if count == n:
                return b
        
        # Generate the next Fibonacci number
        a, b = b, a + b


# Example usage:
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

This script first checks if a number is prime using the `is_prime` function. It then uses this function in the `prime_fib` function to find the n-th prime Fibonacci number. The `prime_fib` function generates Fibonacci numbers until it finds the n-th prime one.