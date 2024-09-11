Here's a Python script that solves the problem using a function to check if a number is prime and another function to generate Fibonacci numbers:

```python
def is_prime(num: int) -> bool:
    """
    is_prime checks if a number is prime.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The n-th prime Fibonacci number.

    Examples:
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    a, b = 0, 1
    prime_index = 1
    while prime_index < n:
        a, b = b, a + b
        if is_prime(b):
            prime_index += 1
    return b


if __name__ == "__main__":
    # Test the prime_fib function
    print(prime_fib(1))  # Should print: 2
    print(prime_fib(2))  # Should print: 3
    print(prime_fib(3))  # Should print: 5
    print(prime_fib(4))  # Should print: 13
    print(prime_fib(5))  # Should print: 89
```

In the code above, `is_prime` function checks whether a given number is prime or not, and `prime_fib` function generates Fibonacci numbers until it finds the nth prime Fibonacci number. The Fibonacci numbers are generated on the fly, and the `is_prime` function is called for each new Fibonacci number to check if it's prime.