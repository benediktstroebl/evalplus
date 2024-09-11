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


def fibonacci():
    """
    Generates Fibonacci numbers.
    
    Yields:
    int: The next Fibonacci number.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    fib_gen = fibonacci()
    count = 0
    while True:
        num = next(fib_gen)
        if is_prime(num):
            count += 1
            if count == n:
                return num


if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

This Python script defines three functions: `is_prime` checks if a number is prime, `fibonacci` generates Fibonacci numbers, and `prime_fib` finds the nth Fibonacci number that is also prime. It then tests `prime_fib` with inputs from 1 to 5, as specified in the example usage.