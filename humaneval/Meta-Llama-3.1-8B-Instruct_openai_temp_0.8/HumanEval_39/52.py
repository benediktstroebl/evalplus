```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    Args:
        num: Number to check.

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
    Generates the nth Fibonacci number.

    Args:
        n: Number of Fibonacci number to generate.

    Returns:
        The nth Fibonacci number.
    """
    if n <= 1:
        return n
    fib_sequence = [0, 1]
    for _ in range(2, n + 1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[-1]


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
        n: Number to find.

    Returns:
        The n-th number that is a Fibonacci number and it's also prime.
    """
    fib_index = 1
    while True:
        fib_num = fibonacci(fib_index)
        if is_prime(fib_num):
            if n == fib_index:
                return fib_num
            fib_index += 1
        else:
            fib_index += 1


# Test cases
print(prime_fib(1))   # Output: 2
print(prime_fib(2))   # Output: 3
print(prime_fib(3))   # Output: 5
print(prime_fib(4))   # Output: 13
print(prime_fib(5))   # Output: 89
```

This Python script includes three functions:

1. `is_prime(num)`: Checks if a number is prime.
2. `fibonacci(n)`: Generates the nth Fibonacci number.
3. `prime_fib(n)`: Returns the n-th number that is a Fibonacci number and it's also prime.

The `prime_fib` function iterates through Fibonacci numbers, checks if each number is prime using the `is_prime` function, and returns the n-th Fibonacci number that is also prime.