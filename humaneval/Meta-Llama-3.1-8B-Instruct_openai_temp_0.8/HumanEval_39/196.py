### Fibonacci Prime Generator
#### Python Script

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
    n (int): The position of the Fibonacci prime to find.
    
    Returns:
    int: The n-th Fibonacci prime.
    """
    a, b = 0, 1
    count = 0
    while True:
        # Check if the Fibonacci number is prime
        if is_prime(b):
            count += 1
            # If we've found the n-th Fibonacci prime, return it
            if count == n:
                return b
        # Generate the next Fibonacci number
        a, b = b, a + b


# Test cases
if __name__ == "__main__":
    print(prime_fib(1))
    print(prime_fib(2))
    print(prime_fib(3))
    print(prime_fib(4))
    print(prime_fib(5))
```

This script defines two functions: `is_prime` checks if a number is prime, and `prime_fib` generates Fibonacci numbers and checks if they are prime, returning the n-th Fibonacci prime. The test cases at the end demonstrate the function's usage.