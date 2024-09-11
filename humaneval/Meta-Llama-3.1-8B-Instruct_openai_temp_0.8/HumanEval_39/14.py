### Prime Fibonacci Numbers
#### A Python Script to Generate Prime Fibonacci Numbers

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


def is_fibonacci(num: int) -> bool:
    """
    Checks if a number is a Fibonacci number.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is a Fibonacci number, False otherwise.
    """
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the number to find.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    count = 0
    num = 0
    while True:
        num += 1
        if is_fibonacci(num) and is_prime(num):
            count += 1
            if count == n:
                return num


if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

This script defines a function `prime_fib(n)` that returns the n-th prime Fibonacci number. The function uses helper functions `is_prime(num)` to check if a number is prime and `is_fibonacci(num)` to check if a number is a Fibonacci number. The script then tests the `prime_fib(n)` function for n = 1 to 5 and prints the results.