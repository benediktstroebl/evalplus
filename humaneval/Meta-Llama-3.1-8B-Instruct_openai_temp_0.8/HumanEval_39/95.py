### Prime Fibonacci Number Generator
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


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    a, b = 0, 1
    fib_num = 1
    while fib_num <= n:
        a, b = b, a + b
        if is_prime(b):
            fib_num += 1
    return b


# Example usage:
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```
This script defines two functions: `is_prime` checks if a number is prime, and `prime_fib` generates Fibonacci numbers and checks if they are prime. The `prime_fib` function uses the `is_prime` function to find the n-th prime Fibonacci number. The example usage at the end demonstrates how to use the `prime_fib` function.