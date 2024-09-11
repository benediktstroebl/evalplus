### prime_fib.py

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


def nth_prime_fib(n: int) -> int:
    """
    Finds the nth Fibonacci number that is also prime.
    
    Args:
    n (int): The position of the Fibonacci number to find.
    
    Returns:
    int: The nth Fibonacci number that is also prime.
    """
    a, b = 0, 1
    prime_count = 0
    while True:
        if is_prime(b):
            prime_count += 1
            if prime_count == n:
                return b
        a, b = b, a + b


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number to find.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    return nth_prime_fib(n)


# Example usage
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

This script defines a function `is_prime` to check if a number is prime, a function `nth_prime_fib` to find the nth Fibonacci number that is also prime, and a function `prime_fib` that simply calls `nth_prime_fib`. The script includes example usage at the end to demonstrate how to use the `prime_fib` function.