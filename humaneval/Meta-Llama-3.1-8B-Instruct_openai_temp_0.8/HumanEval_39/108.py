### Fibonacci Prime Generator
#### Python Script

```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    Args:
        num (int): Number to check.

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
        n (int): Index of the Fibonacci number to generate.

    Returns:
        int: The n-th Fibonacci number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[-1]


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
        n (int): Index of the Fibonacci prime to return.

    Returns:
        int: The n-th Fibonacci prime.
    """
    count = 0
    i = 1
    while count < n:
        num = fibonacci(i)
        if is_prime(num):
            count += 1
            if count == n:
                return num
        i += 1


# Example usage
print(prime_fib(1))   # Output: 2
print(prime_fib(2))   # Output: 3
print(prime_fib(3))   # Output: 5
print(prime_fib(4))   # Output: 13
print(prime_fib(5))   # Output: 89
```

Note that this script uses a naive approach to generate Fibonacci numbers and check for primality. For larger values of `n`, you may want to use more efficient algorithms, such as the matrix exponentiation method for Fibonacci numbers and the AKS primality test or the Miller-Rabin primality test for primality checks.