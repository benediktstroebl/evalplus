```python
def is_prime(num: int) -> bool:
    """
    Check if a number is prime.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def fibonacci(n: int) -> int:
    """
    Return the n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to return.

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
    Return the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the number to return.

    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            if n == 1:
                return fib_num
            n -= 1
        i += 1


# Example usage
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script uses three separate functions to check if a number is prime (`is_prime`), to calculate the n-th Fibonacci number (`fibonacci`), and to find the n-th Fibonacci number that is also prime (`prime_fib`). The `prime_fib` function uses a loop to calculate Fibonacci numbers and checks each one to see if it's prime, returning the first prime Fibonacci number for each value of `n`.