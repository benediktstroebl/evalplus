```python
def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    Generates the n-th Fibonacci number.
    
    Args:
    n (int): The position of the Fibonacci number.
    
    Returns:
    int: The n-th Fibonacci number.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        for _ in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the number.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    count = 0
    num = 0
    while count < n:
        num = fibonacci(num + 1)
        if is_prime(num):
            count += 1
    return num


# Example usage:
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script defines three functions: `is_prime` to check if a number is prime, `fibonacci` to generate the n-th Fibonacci number, and `prime_fib` to find the n-th Fibonacci number that is also prime. The `prime_fib` function uses a while loop to generate Fibonacci numbers until it finds the n-th one that is also prime.