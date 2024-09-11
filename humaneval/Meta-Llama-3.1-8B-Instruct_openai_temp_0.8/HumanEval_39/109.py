```python
def is_prime(num: int) -> bool:
    """
    Helper function to check if a number is prime.
    
    Args:
    num (int): The number to check.
    
    Returns:
    bool: True if num is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The index of the Fibonacci number to find.
    
    Returns:
    int: The nth Fibonacci number that is also prime.
    """
    a, b = 0, 1
    count = 0
    i = 1
    
    while count < n:
        if is_prime(b):
            count += 1
            if count == n:
                return b
        a, b = b, a + b
        i += 1

print("Testing prime_fib function:")
print(prime_fib(1))  # Expected output: 2
print(prime_fib(2))  # Expected output: 3
print(prime_fib(3))  # Expected output: 5
print(prime_fib(4))  # Expected output: 13
print(prime_fib(5))  # Expected output: 89
```

This script first checks if a number is prime using the `is_prime` function, and then it calculates the nth Fibonacci number using a generator approach. It keeps track of the number of prime Fibonacci numbers found so far and stops when it finds the nth one.