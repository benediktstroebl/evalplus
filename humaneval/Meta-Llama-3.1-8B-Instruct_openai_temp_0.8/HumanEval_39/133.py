### Fibonacci Prime Generator
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


def fibonacci():
    """
    Generates Fibonacci numbers indefinitely.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    """
    fibonacci_gen = fibonacci()
    count = 0
    num = 0
    for fib_num in fibonacci_gen:
        num = fib_num
        if is_prime(fib_num):
            count += 1
            if count == n:
                return num
```

### Example Usage
```python
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script defines a generator function `fibonacci()` to produce Fibonacci numbers on the fly. The `is_prime()` function checks if a number is prime, and the `prime_fib()` function uses these two helper functions to find the n-th Fibonacci number that is also prime. The usage example demonstrates the function with various inputs.