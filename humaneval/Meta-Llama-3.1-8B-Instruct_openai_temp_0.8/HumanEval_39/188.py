```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.
    
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

def fibonacci(n: int) -> int:
    """
    Generates the nth Fibonacci number.
    
    Args:
    n (int): The position of the Fibonacci number.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

def prime_fib(n: int) -> int:
    """
    Returns the nth Fibonacci number that is also prime.
    
    Args:
    n (int): The position of the Fibonacci number.
    
    Returns:
    int: The nth Fibonacci number that is prime.
    """
    count = 0
    num = 1
    while True:
        fib_num = fibonacci(num)
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num
        num += 1

# Example usage:
print(prime_fib(1))
print(prime_fib(2))
print(prime_fib(3))
print(prime_fib(4))
print(prime_fib(5))
```

This script uses a separate function to check if a number is prime (`is_prime`) and another function to generate the nth Fibonacci number (`fibonacci`). The `prime_fib` function then uses these two functions to find the nth Fibonacci number that is also prime.