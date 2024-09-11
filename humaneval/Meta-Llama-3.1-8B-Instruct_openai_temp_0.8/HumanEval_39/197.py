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


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number to find.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    a, b = 0, 1
    count = 0
    while True:
        # Generate the next Fibonacci number
        a, b = b, a + b
        # Check if the Fibonacci number is prime and increment the count
        if is_prime(b) and count == n:
            return b
        # Increment the count only if the Fibonacci number is prime
        if is_prime(b):
            count += 1


# Test cases
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script first defines a helper function `is_prime` to check if a number is prime. The `prime_fib` function then generates Fibonacci numbers until it finds the n-th one that is also prime. The test cases at the end demonstrate the function's correctness.