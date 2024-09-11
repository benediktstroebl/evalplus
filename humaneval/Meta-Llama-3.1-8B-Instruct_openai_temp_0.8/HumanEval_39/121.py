```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    Args:
    num (int): Number to check for primality.

    Returns:
    bool: True if num is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def fib(n: int) -> int:
    """
    Generates the nth Fibonacci number.

    Args:
    n (int): Position of the Fibonacci number to generate.

    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): Position of the Fibonacci number to generate.

    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    count = 0
    num = 1
    while True:
        fib_num = fib(num)
        if fib_num > 0 and is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num
        num += 1


# Example usage:
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script defines three functions:

- `is_prime(num)`: checks if a number is prime.
- `fib(n)`: generates the nth Fibonacci number.
- `prime_fib(n)`: finds the nth Fibonacci number that is also prime.

The `prime_fib(n)` function works by continuously generating Fibonacci numbers and checking if they are prime. It keeps track of the count of prime Fibonacci numbers and returns the nth prime Fibonacci number when it is found.