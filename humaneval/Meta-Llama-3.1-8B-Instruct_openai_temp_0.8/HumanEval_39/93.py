```markdown
### Prime Fibonacci Number Generator

This Python script generates the n-th number that is both a Fibonacci number and a prime number.

#### Code
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
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the prime Fibonacci number to generate.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    current_n = 1
    while True:
        fib_num = fibonacci(current_n)
        if is_prime(fib_num):
            if current_n == n:
                return fib_num
        current_n += 1


# Example usage:
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"Prime Fibonacci number at position {i}: {prime_fib(i)}")
```

#### Explanation
This script defines three functions:

*   `is_prime(num)`: Checks whether a given number is prime.
*   `fibonacci(n)`: Generates the nth Fibonacci number.
*   `prime_fib(n)`: Finds the n-th Fibonacci number that is also prime.

The `prime_fib(n)` function uses a loop to generate Fibonacci numbers and checks each one for primality using the `is_prime(num)` function. When it finds the n-th prime Fibonacci number, it returns it.

In the example usage, we print the first five prime Fibonacci numbers.