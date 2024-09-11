### Prime Fibonacci Numbers
#### Python Script

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
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def fibonacci(n: int) -> int:
    """
    Generates the nth Fibonacci number.
    
    Args:
    n (int): The position of the Fibonacci number.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number.
    
    Returns:
    int: The n-th prime Fibonacci number.
    """
    fib_num = 1
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            if n == 1:
                return fib_num
            n -= 1
        i += 1

# Test cases
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script defines three functions:

1.  `is_prime(n)`: Checks if a number `n` is prime.
2.  `fibonacci(n)`: Generates the nth Fibonacci number.
3.  `prime_fib(n)`: Returns the n-th number that is a Fibonacci number and it's also prime.

The `prime_fib(n)` function uses a loop to generate Fibonacci numbers and checks if they are prime using the `is_prime(n)` function. It continues this process until it finds the n-th prime Fibonacci number. The test cases at the end demonstrate its usage.