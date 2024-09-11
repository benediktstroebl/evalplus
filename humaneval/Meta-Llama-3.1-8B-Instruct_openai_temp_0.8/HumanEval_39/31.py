### Fibonacci and Prime Number Generator
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
    Generates Fibonacci numbers.
    
    Yields:
    int: Fibonacci numbers in ascending order.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_fib(n: int) -> int:
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number.
    
    Returns:
    int: The n-th Fibonacci number that is prime.
    """
    fib_gen = fibonacci()
    count = 0
    for num in fib_gen:
        if is_prime(num):
            count += 1
            if count == n:
                return num


# Example usage:
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```
This script defines a function `prime_fib` that generates Fibonacci numbers and checks if they are prime. It uses a generator to produce Fibonacci numbers and the `is_prime` function to check for primality. The `prime_fib` function returns the n-th Fibonacci number that is prime. The example usage at the end demonstrates how to use the `prime_fib` function.