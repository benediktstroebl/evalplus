### prime_fib Function
```python
def is_prime(num: int) -> bool:
    """
    Helper function to check if a number is prime.
    
    Args:
    num (int): The number to check.
    
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
    n (int): The position of the Fibonacci number.
    
    Returns:
    int: The n-th prime Fibonacci number.
    """
    fib_index, a, b = 0, 0, 1
    while fib_index < n:
        a, b = b, a + b
        if is_prime(b):
            fib_index += 1
    return b


# Example usage:
print(prime_fib(1))   # Output: 2
print(prime_fib(2))   # Output: 3
print(prime_fib(3))   # Output: 5
print(prime_fib(4))   # Output: 13
print(prime_fib(5))   # Output: 89
```
This script defines a helper function `is_prime` to check if a number is prime, and the `prime_fib` function to generate the n-th prime Fibonacci number. The `prime_fib` function uses the property of Fibonacci numbers to efficiently generate and check each number. It keeps track of the current Fibonacci number and its index, and increments the index whenever it finds a prime number.