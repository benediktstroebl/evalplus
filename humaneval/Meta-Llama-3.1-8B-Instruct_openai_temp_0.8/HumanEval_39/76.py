```markdown
### prime_fib.py
#### A Python script that finds the nth Fibonacci number that is also prime

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


def prime_fib(n: int):
    """
    Returns the nth number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The index of the Fibonacci number.

    Returns:
    int: The nth Fibonacci number that is also prime.
    """
    a, b = 0, 1
    prime_count = 0
    while prime_count < n:
        a, b = b, a + b
        if is_prime(b):
            prime_count += 1
    return b


# Test cases
print(prime_fib(1))  # Should print 2
print(prime_fib(2))  # Should print 3
print(prime_fib(3))  # Should print 5
print(prime_fib(4))  # Should print 13
print(prime_fib(5))  # Should print 89
```

This script defines two helper functions: `is_prime` checks whether a number is prime, and `prime_fib` generates Fibonacci numbers until it finds the nth prime one. The test cases at the end verify the correctness of the `prime_fib` function.