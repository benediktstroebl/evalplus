```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.
    
    Args:
    num: The number to check.
    
    Returns:
    True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n: The position of the number in the sequence.
    
    Returns:
    The n-th number that is a Fibonacci number and it's also prime.
    """
    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a + b
        if is_prime(b):
            count += 1
        if count == n:
            return b


# Test cases
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script defines two functions: `is_prime` checks if a number is prime, and `prime_fib` generates Fibonacci numbers and checks if they're prime. It keeps generating Fibonacci numbers until it finds the n-th one that's also prime.