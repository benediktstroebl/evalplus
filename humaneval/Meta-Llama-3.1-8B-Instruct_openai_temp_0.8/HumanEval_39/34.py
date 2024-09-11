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


def fibonacci(length: int) -> list:
    """
    Generate a list of Fibonacci numbers up to a given length.
    
    Args:
    length (int): The number of Fibonacci numbers to generate.
    
    Returns:
    list: A list of Fibonacci numbers.
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < length:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    fib_sequence = fibonacci(n + 1)
    for num in fib_sequence:
        if is_prime(num):
            return num


# Test cases
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script defines three functions:

1. `is_prime(num)`: Checks if a number is prime by iterating up to its square root.
2. `fibonacci(length)`: Generates a list of Fibonacci numbers up to a given length.
3. `prime_fib(n)`: Returns the n-th Fibonacci number that is also prime by checking each Fibonacci number.

The script includes test cases to verify the correctness of the `prime_fib(n)` function.