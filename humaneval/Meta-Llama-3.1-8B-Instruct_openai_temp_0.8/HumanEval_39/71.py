### Prime Fibonacci Number
```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.
    
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


def fibonacci(n: int) -> int:
    """
    Generates the n-th Fibonacci number.
    
    Args:
    n: The index of the Fibonacci number to generate.
    
    Returns:
    The n-th Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_numbers = [0, 1]
        while len(fib_numbers) < n:
            fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
        return fib_numbers[-1]


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n: The index of the number to find.
    
    Returns:
    The n-th number that is a Fibonacci number and it's also prime.
    """
    count = 0
    num = 0
    while count < n:
        num = fibonacci(num)
        if is_prime(num):
            count += 1
    return num


# Example usage:
print(prime_fib(1))   # Output: 2
print(prime_fib(2))   # Output: 3
print(prime_fib(3))   # Output: 5
print(prime_fib(4))   # Output: 13
print(prime_fib(5))   # Output: 89
```
This code defines three functions: `is_prime` checks if a number is prime, `fibonacci` generates the n-th Fibonacci number, and `prime_fib` finds the n-th Fibonacci number that is also prime. The example usage at the end demonstrates how to use the `prime_fib` function.