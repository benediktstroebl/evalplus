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
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci() -> list:
    """
    Generates a list of Fibonacci numbers.
    
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
    int: The n-th prime Fibonacci number.
    """
    fib_gen = fibonacci()
    count = 0
    while True:
        num = next(fib_gen)
        if is_prime(num):
            count += 1
            if count == n:
                return num


# Test the function
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

This script defines three functions: `is_prime` checks if a number is prime, `fibonacci` generates a list of Fibonacci numbers, and `prime_fib` finds the n-th prime Fibonacci number. The `prime_fib` function uses a generator to produce Fibonacci numbers and checks each one to see if it's prime. Once it finds the n-th prime Fibonacci number, it returns it.