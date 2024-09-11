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
    Returns the n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    num = 1
    while True:
        fib_num = fibonacci(num)
        if is_prime(fib_num):
            if n == 1:
                return fib_num
            n -= 1
        num += 1


# Example usage:
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

This script first defines a helper function `is_prime` to check if a number is prime. It then defines a recursive function `fibonacci` to calculate the n-th Fibonacci number. Finally, it defines the main function `prime_fib` to find the n-th number that is a Fibonacci number and it's also prime. The script also includes example usage in the `if __name__ == "__main__":` block.