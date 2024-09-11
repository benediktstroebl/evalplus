### Prime Fibonacci Numbers

Below is a Python function that generates the `n-th` number that is a Fibonacci number and it's also prime.

```markdown
### Code
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
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci():
    """
    Generates Fibonacci numbers.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the number in the sequence.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    fib_gen = fibonacci()
    count = 0
    num = 0
    while count < n:
        num = next(fib_gen)
        if is_prime(num):
            count += 1
    return num


# Example usage:
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

### Explanation

The `prime_fib` function relies on two helper functions: `is_prime` and `fibonacci`.

- `is_prime` checks whether a number is prime by testing divisibility up to its square root.
- `fibonacci` generates Fibonacci numbers indefinitely. The generator approach allows us to yield numbers one at a time, which is memory-efficient.

The `prime_fib` function iterates over the Fibonacci sequence and checks each number for primality using the `is_prime` function. It keeps track of the count of prime Fibonacci numbers encountered and returns the `n-th` such number.