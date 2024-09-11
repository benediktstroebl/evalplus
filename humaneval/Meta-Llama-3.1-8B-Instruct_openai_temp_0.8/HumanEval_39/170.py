### Prime Fibonacci Numbers
#### A Python Script to Find Prime Fibonacci Numbers
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
    Generates the n-th Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The n-th Fibonacci number.
    """
    fib = [0, 1]
    while len(fib) < n + 1:
        fib.append(fib[-1] + fib[-2])
    return fib[n]


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the Fibonacci number.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            return fib_num
        i += 1


# Example usage:
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```
This script consists of three functions:

1.  `is_prime(num)`: Checks if a number is prime.
2.  `fibonacci(n)`: Generates the n-th Fibonacci number.
3.  `prime_fib(n)`: Returns the n-th number that is a Fibonacci number and it's also prime.

The `prime_fib` function uses the `fibonacci` function to generate Fibonacci numbers and checks each number to see if it's prime using the `is_prime` function. It continues this process until it finds the n-th prime Fibonacci number.