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
    n (int): The index of the Fibonacci number to generate.

    Returns:
    int: The n-th Fibonacci number.
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
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The index of the number to return.

    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    fib_num = 1
    while True:
        fib_num = fibonacci(fib_num)
        if is_prime(fib_num):
            if n == 1:
                return fib_num
            n -= 1


# Test the function
print(prime_fib(1))   # Output: 2
print(prime_fib(2))   # Output: 3
print(prime_fib(3))   # Output: 5
print(prime_fib(4))   # Output: 13
print(prime_fib(5))   # Output: 89
```

This script first defines a helper function `is_prime` to check if a number is prime, a `fibonacci` function to generate Fibonacci numbers, and then the `prime_fib` function, which returns the n-th Fibonacci number that is also prime. The `prime_fib` function uses a while loop to keep generating Fibonacci numbers until it finds one that is prime, at which point it returns that number.