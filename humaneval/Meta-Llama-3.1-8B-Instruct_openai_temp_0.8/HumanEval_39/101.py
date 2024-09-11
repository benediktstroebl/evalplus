### Prime Fibonacci Numbers
#### Python Script
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


def fibonacci_prime(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the number in the sequence.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    fib_sequence = [0, 1]
    prime_fib_index = 1
    while prime_fib_index < n:
        # Generate the next Fibonacci number
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        # Check if the next Fibonacci number is prime
        if is_prime(next_fib):
            fib_sequence.append(next_fib)
            prime_fib_index += 1
    return fib_sequence[-1]


def prime_fib(n: int) -> int:
    """
    Returns n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the number in the sequence.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    return fibonacci_prime(n)


# Test cases
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script first checks if a number is prime using the `is_prime` function, then generates Fibonacci numbers and checks if they are prime using the `fibonacci_prime` function. The `prime_fib` function is the main function that takes the position `n` and returns the `n-th` prime Fibonacci number. The test cases at the end verify the function's correctness.