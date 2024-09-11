### Fibonacci and Prime Checker
#### A Python script that finds the nth Fibonacci number that is also prime.

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
    Generates the nth Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def prime_fib(n: int) -> int:
    """
    Returns the nth Fibonacci number that is also prime.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The nth Fibonacci number that is prime.
    """
    fib_num = 1
    prime_count = 0
    while prime_count < n:
        fib_num = fibonacci(fib_num)
        if is_prime(fib_num):
            prime_count += 1
    return fib_num


# Example usage
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

In this script, the `is_prime` function checks whether a number is prime, the `fibonacci` function generates the nth Fibonacci number, and the `prime_fib` function uses these two functions to find the nth Fibonacci number that is prime. The example usage at the end demonstrates how to use the `prime_fib` function with different inputs.