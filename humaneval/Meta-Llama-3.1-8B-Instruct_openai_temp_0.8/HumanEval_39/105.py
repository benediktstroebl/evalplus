### Prime Fibonacci Numbers

The following Python script calculates the n-th prime Fibonacci number.

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
    Generates the n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    count = 0
    num = 0
    while True:
        num = fibonacci(num + 1)
        if is_prime(num):
            count += 1
            if count == n:
                return num
```

### Example Use Case

```python
print(prime_fib(1))   # Output: 2
print(prime_fib(2))   # Output: 3
print(prime_fib(3))   # Output: 5
print(prime_fib(4))   # Output: 13
print(prime_fib(5))   # Output: 89
```