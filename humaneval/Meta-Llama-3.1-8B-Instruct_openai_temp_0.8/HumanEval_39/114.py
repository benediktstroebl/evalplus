### Prime Fibonacci Numbers

Below is a Python script that generates the n-th prime Fibonacci number.

```python
def is_prime(n: int) -> bool:
    """
    Helper function to check if a number is prime.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    Generate the n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 0:
        return "Input should be a positive integer."

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[-1]


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the prime Fibonacci number.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    fib_count = 1
    while True:
        fib_num = fibonacci(fib_count)
        if is_prime(fib_num):
            return fib_num
        fib_count += 1


# Example usage:
for i in range(1, 6):
    print(f"Prime Fibonacci number at position {i}: {prime_fib(i)}")
```

This script uses a helper function `is_prime` to check if a number is prime, and a function `fibonacci` to generate Fibonacci numbers. The `prime_fib` function continuously generates Fibonacci numbers and checks if they are prime until it finds the n-th prime Fibonacci number.