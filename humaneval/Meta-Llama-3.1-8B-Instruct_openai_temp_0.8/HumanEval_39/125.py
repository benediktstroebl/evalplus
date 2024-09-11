### Python Script to Find the nth Prime Fibonacci Number
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
    Returns the nth Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def prime_fib(n: int) -> int:
    """
    Returns the nth number that is a Fibonacci number and it's also prime.

    Args:
        n (int): The index of the Fibonacci number.

    Returns:
        int: The nth prime Fibonacci number.
    """
    count = 0
    num = 0
    while True:
        num = fibonacci(num + 1)
        if is_prime(num):
            count += 1
            if count == n:
                return num


# Example usage:
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

This script first defines helper functions `is_prime` and `fibonacci`, then the main function `prime_fib`. The `is_prime` function checks if a number is prime, the `fibonacci` function calculates the nth Fibonacci number, and the `prime_fib` function returns the nth prime Fibonacci number by iterating through Fibonacci numbers and checking if they are prime. The example usage at the end shows how to use the `prime_fib` function.