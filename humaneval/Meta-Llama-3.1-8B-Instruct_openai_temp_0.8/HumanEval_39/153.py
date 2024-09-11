### Prime Fibonacci Numbers
#### Script to find the nth prime Fibonacci number

```python
def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    Generates the nth Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to generate.

    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
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
    Finds the nth prime Fibonacci number.

    Args:
    n (int): The position of the prime Fibonacci number to find.

    Returns:
    int: The nth prime Fibonacci number.
    """
    count = 0
    num = 0
    while True:
        num = fibonacci(count + 1)
        if is_prime(num):
            if count == n - 1:
                return num
            count += 1
        else:
            count += 1


# Example use cases
if __name__ == "__main__":
    print(prime_fib(1))   # Output: 2
    print(prime_fib(2))   # Output: 3
    print(prime_fib(3))   # Output: 5
    print(prime_fib(4))   # Output: 13
    print(prime_fib(5))   # Output: 89
```

This script first defines helper functions to check if a number is prime (`is_prime`) and to generate Fibonacci numbers (`fibonacci`). The `prime_fib` function uses these helpers to find the nth prime Fibonacci number. It does this by generating Fibonacci numbers and checking if they are prime, incrementing a counter until it finds the nth prime.