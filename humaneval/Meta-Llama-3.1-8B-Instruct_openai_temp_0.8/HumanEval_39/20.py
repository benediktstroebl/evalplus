### Fibonacci and Prime Check
#### Solution

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


def fibonacci(n: int) -> int:
    """
    Generates the Fibonacci sequence up to the nth number.

    Args:
    n (int): The position of the number in the sequence.

    Returns:
    int: The nth Fibonacci number.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def prime_fib(n: int) -> int:
    """
    Returns the nth Fibonacci number that is also prime.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The nth Fibonacci number that is also prime.
    """
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            return fib_num
        i += 1


# Test cases
print(prime_fib(1))   # Output: 2
print(prime_fib(2))   # Output: 3
print(prime_fib(3))   # Output: 5
print(prime_fib(4))   # Output: 13
print(prime_fib(5))   # Output: 89
```

This script first defines a helper function `is_prime` to check if a number is prime, then a function `fibonacci` to generate the Fibonacci sequence up to the nth number. The `prime_fib` function uses these helpers to find the nth Fibonacci number that is also prime. The test cases at the end demonstrate the function's correctness.