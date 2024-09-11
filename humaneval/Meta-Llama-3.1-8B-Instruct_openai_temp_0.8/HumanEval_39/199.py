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
    Generates the nth Fibonacci number.
    
    Args:
    n (int): The position of the Fibonacci number to generate.
    
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
    n (int): The position of the Fibonacci number to find.
    
    Returns:
    int: The n-th Fibonacci prime number.
    """
    count = 0
    i = 1
    while True:
        fib = fibonacci(i)
        if is_prime(fib):
            count += 1
            if count == n:
                return fib
        i += 1


# Example usage:
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

This script first defines a helper function `is_prime` to check if a number is prime, then a `fibonacci` function to generate Fibonacci numbers, and finally the `prime_fib` function that uses these two to find the n-th Fibonacci prime number. The example usage demonstrates how to use this function to find the 1st to 5th Fibonacci prime numbers.