### Prime Fibonacci Numbers
#### Python Script
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
    Returns the nth Fibonacci number.
    
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
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]


def prime_fib(n: int) -> int:
    """
    Returns the nth prime Fibonacci number.
    
    Args:
    n (int): The position of the prime Fibonacci number.
    
    Returns:
    int: The nth prime Fibonacci number.
    """
    count = 0
    i = 0
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num
        i += 1


# Example usage:
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```
This script defines three functions: `is_prime`, `fibonacci`, and `prime_fib`. The `is_prime` function checks if a number is prime, the `fibonacci` function generates Fibonacci numbers, and the `prime_fib` function returns the nth prime Fibonacci number. The example usage at the end demonstrates how to use the `prime_fib` function.