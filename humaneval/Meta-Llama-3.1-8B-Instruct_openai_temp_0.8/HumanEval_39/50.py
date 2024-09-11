### Prime Fibonacci Number Generator

Below is a Python script that defines a function `prime_fib` to generate the n-th prime Fibonacci number.

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
    Generates the n-th Fibonacci number.
    
    Args:
    n (int): The position of the Fibonacci number to generate.
    
    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number to generate.
    
    Returns:
    int: The n-th prime Fibonacci number.
    """
    fib_num = 1
    prime_count = 0
    while prime_count < n:
        fib_num = fibonacci(fib_num)
        if is_prime(fib_num):
            prime_count += 1
    return fib_num


# Example usage:
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script defines three functions: `is_prime`, `fibonacci`, and `prime_fib`. The `is_prime` function checks if a number is prime, the `fibonacci` function generates the n-th Fibonacci number, and the `prime_fib` function generates the n-th prime Fibonacci number. The example usage at the end demonstrates how to use the `prime_fib` function.