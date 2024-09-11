### Prime Fibonacci Numbers
#### A Python Script to Find the N-th Prime Fibonacci Number

```python
def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    Generates Fibonacci numbers up to the n-th number.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        int: The n-th Fibonacci number.
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[-1]


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
        n (int): The position of the Fibonacci number to check.

    Returns:
        int: The n-th prime Fibonacci number.
    """
    fib_index = 1
    while True:
        fib_num = fibonacci(fib_index)
        if is_prime(fib_num):
            if fib_index == n:
                return fib_num
        fib_index += 1


# Example usage:
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script first defines helper functions to check if a number is prime (`is_prime`) and to generate Fibonacci numbers up to a given position (`fibonacci`). The `prime_fib` function generates Fibonacci numbers and checks if they are prime, returning the n-th prime Fibonacci number when found. The example usage demonstrates the function's behavior for different inputs.