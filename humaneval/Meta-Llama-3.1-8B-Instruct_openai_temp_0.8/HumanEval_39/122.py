### Fibonacci Prime Generator

This script generates the `n-th` Fibonacci number that is also prime.

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
    Generates a sequence of Fibonacci numbers.
    
    Yields:
    int: The next Fibonacci number in the sequence.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci prime to find.
    
    Returns:
    int: The n-th Fibonacci prime number.
    """
    fib_gen = fibonacci()
    count = 0
    num = 0
    while True:
        num = next(fib_gen)
        if is_prime(num):
            count += 1
            if count == n:
                return num


# Example usage:
print(prime_fib(1))   # Output: 2
print(prime_fib(2))   # Output: 3
print(prime_fib(3))   # Output: 5
print(prime_fib(4))   # Output: 13
print(prime_fib(5))   # Output: 89
```

This script uses the following functions:

- `is_prime(num)`: Checks if a number is prime.
- `fibonacci()`: Generates a sequence of Fibonacci numbers.
- `prime_fib(n)`: Finds the `n-th` Fibonacci number that is also prime.

The `prime_fib(n)` function uses a generator function `fibonacci()` to yield Fibonacci numbers and checks each number to see if it's prime using the `is_prime(num)` function. The first prime Fibonacci number found is returned when it reaches the desired position `n`.