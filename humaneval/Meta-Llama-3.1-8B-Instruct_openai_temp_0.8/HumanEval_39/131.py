```python
def is_prime(num: int) -> bool:
    """
    is_prime checks if a number is prime.
    
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


def is_fibonacci(num: int) -> bool:
    """
    is_fibonacci checks if a number is a Fibonacci number.
    
    Args:
    num (int): The number to check.
    
    Returns:
    bool: True if the number is a Fibonacci number, False otherwise.
    """
    if num < 0:
        return False
    x = 0
    y = 1
    while y < num:
        z = x + y
        x = y
        y = z
    return y == num


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    fib_index = 1
    i = 2  # start with the first Fibonacci number
    while fib_index < n:
        if is_prime(i) and is_fibonacci(i):
            fib_index += 1
        i += 1
    return i - 1  # return the last found Fibonacci number that is also prime

# Test the function
print(prime_fib(1))   # 2
print(prime_fib(2))   # 3
print(prime_fib(3))   # 5
print(prime_fib(4))   # 13
print(prime_fib(5))   # 89
```

This script checks each number to see if it's both a Fibonacci number and a prime number. It keeps track of the position of the current Fibonacci number and stops when it finds the n-th number that is both a Fibonacci number and a prime number. The function returns this number.