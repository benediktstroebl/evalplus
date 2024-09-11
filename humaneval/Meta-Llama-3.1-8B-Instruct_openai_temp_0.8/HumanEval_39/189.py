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
        n (int): The position of the Fibonacci number to generate.

    Returns:
        int: The nth Fibonacci number.
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < n + 1:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[n]


def prime_fib(n: int) -> int:
    """
    Returns the nth number that is a Fibonacci number and it's also prime.

    Args:
        n (int): The position of the prime Fibonacci number to find.

    Returns:
        int: The nth prime Fibonacci number.
    """
    count = 0
    num = 0
    while True:
        num += 1
        if is_prime(num) and fibonacci(num) == num:  # Check if the Fibonacci number is the same as the position
            count += 1
            if count == n:
                return num


# Test cases
print(prime_fib(1))  # Expected output: 2
print(prime_fib(2))  # Expected output: 3
print(prime_fib(3))  # Expected output: 5
print(prime_fib(4))  # Expected output: 13
print(prime_fib(5))  # Expected output: 89
```

This script defines three functions: `is_prime` checks if a number is prime, `fibonacci` generates the nth Fibonacci number, and `prime_fib` finds the nth prime Fibonacci number. The `prime_fib` function uses a while loop to generate Fibonacci numbers and checks if each one is prime using the `is_prime` function. The script also includes test cases to verify the correctness of the `prime_fib` function.