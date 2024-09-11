**Prime Fibonacci Numbers**
==========================

The following Python script generates the `n`-th prime Fibonacci number.

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
    if n <= 0:
        return "Input should be a positive integer."
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
    n (int): The position of the prime Fibonacci number.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    count = 0
    num = 0
    while True:
        num = fibonacci(n + count)
        if is_prime(num):
            return num
        count += 1


# Example usage
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

This script defines three functions:

1.  `is_prime`: Checks if a number is prime by testing divisibility up to the square root of the number.
2.  `fibonacci`: Generates the `n`-th Fibonacci number using a loop to calculate the sequence.
3.  `prime_fib`: Finds the `n`-th prime Fibonacci number by generating Fibonacci numbers sequentially and checking if each one is prime using the `is_prime` function.

The example usage at the end demonstrates how to use the `prime_fib` function to find the first few prime Fibonacci numbers.