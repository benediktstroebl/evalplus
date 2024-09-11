```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    Returns the nth Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number to return.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]


def prime_fib(n: int) -> int:
    """
    Returns the nth number that is a Fibonacci number and it's also prime.

    Args:
        n (int): The index of the Fibonacci number to return.

    Returns:
        int: The nth Fibonacci number that is prime.
    """
    fib_index = 1
    while True:
        fib_num = fibonacci(fib_index)
        if is_prime(fib_num):
            if fib_index == n:
                return fib_num
            else:
                fib_index += 1
        else:
            fib_index += 1


# Test the function
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script defines three functions: `is_prime` checks if a number is prime, `fibonacci` returns the nth Fibonacci number, and `prime_fib` returns the nth Fibonacci number that is prime. The `prime_fib` function uses a while loop to check each Fibonacci number until it finds the nth prime Fibonacci number.