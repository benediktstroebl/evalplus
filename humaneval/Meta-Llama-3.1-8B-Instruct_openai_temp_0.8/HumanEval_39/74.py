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


def fibonacci() -> list:
    """
    Generates a Fibonacci sequence.
    
    Yields:
    list: The next number in the Fibonacci sequence.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The index of the Fibonacci number to find.
    
    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    fib = fibonacci()
    count = 0
    while True:
        num = next(fib)
        if is_prime(num):
            count += 1
            if count == n:
                return num


# Test cases
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

This script uses the `is_prime` function to check if a number is prime and the `fibonacci` generator to generate Fibonacci numbers on-the-fly. The `prime_fib` function uses these two to find the n-th number that is both a Fibonacci number and a prime number. The test cases at the end check the function against the provided examples.