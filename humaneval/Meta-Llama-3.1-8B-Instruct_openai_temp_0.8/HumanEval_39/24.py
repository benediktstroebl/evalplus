```python
def is_prime(num: int) -> bool:
    """
    Helper function to check if a number is prime.
    
    Args:
    num: The number to check.
    
    Returns:
    True if the number is prime, False otherwise.
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
    n: The position of the Fibonacci number to find.
    
    Returns:
    The n-th number that is a Fibonacci number and it's also prime.
    """
    a, b = 0, 1
    count = 0
    while True:
        if is_prime(b):
            count += 1
            if count == n:
                return b
        a, b = b, a + b


# Example usage
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```
This script defines two functions: `is_prime` checks if a number is prime, and `prime_fib` generates Fibonacci numbers and checks if they are prime using the `is_prime` function. It then prints the first five Fibonacci numbers that are also prime.