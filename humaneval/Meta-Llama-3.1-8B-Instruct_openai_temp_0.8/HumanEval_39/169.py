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


def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number to find.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a + b
        if is_prime(b):
            count += 1
    return b


# Test cases
print(prime_fib(1))  # Expected output: 2
print(prime_fib(2))  # Expected output: 3
print(prime_fib(3))  # Expected output: 5
print(prime_fib(4))  # Expected output: 13
print(prime_fib(5))  # Expected output: 89
```

This script first defines a helper function `is_prime` to check if a number is prime. Then it defines the `prime_fib` function, which generates Fibonacci numbers and checks each one for primality until it finds the n-th such number. The test cases at the end verify the correctness of the `prime_fib` function.