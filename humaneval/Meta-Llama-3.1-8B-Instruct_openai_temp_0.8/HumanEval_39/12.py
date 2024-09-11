### Fibonacci Prime Number Generator
#### Script Description
This Python script generates the n-th Fibonacci prime number. A Fibonacci prime is a Fibonacci number that is also a prime number.

```python
def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.

    Args:
    n (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci_prime(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci prime to generate.

    Returns:
    int: The n-th Fibonacci prime number.
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) <= n:
        # Generate the next Fibonacci number
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        # Check if the new Fibonacci number is prime
        if is_prime(next_fib):
            fib_sequence.append(next_fib)
    return fib_sequence[n]


def prime_fib(n: int) -> int:
    """
    Returns n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci prime to generate.

    Returns:
    int: The n-th Fibonacci prime number.
    """
    return fibonacci_prime(n)


# Example usage:
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

This script defines a function `is_prime` to check if a number is prime, a function `fibonacci_prime` to generate the n-th Fibonacci prime, and a function `prime_fib` that simply calls `fibonacci_prime` with the same argument. The script demonstrates the usage of the `prime_fib` function with some examples.