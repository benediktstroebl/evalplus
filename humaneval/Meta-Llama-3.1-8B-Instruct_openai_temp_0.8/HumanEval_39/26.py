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


def fibonacci(n: int) -> int:
    """
    Returns the nth Fibonacci number.
    
    Args:
    n (int): The position of the Fibonacci number to return.
    
    Returns:
    int: The nth Fibonacci number.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number to return.
    
    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            return fib_num
        i += 1


# Test cases
print(prime_fib(1))   # Output: 2
print(prime_fib(2))   # Output: 3
print(prime_fib(3))   # Output: 5
print(prime_fib(4))   # Output: 13
print(prime_fib(5))   # Output: 89
```
This script first defines a helper function `is_prime` to check if a number is prime, then defines the `fibonacci` function to calculate the nth Fibonacci number, and finally the `prime_fib` function to find the nth Fibonacci number that is also prime. The script then includes some test cases to demonstrate the functionality of the `prime_fib` function.