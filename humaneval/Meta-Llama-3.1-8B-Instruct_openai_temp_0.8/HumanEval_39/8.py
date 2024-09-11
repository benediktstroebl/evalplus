### Prime Fibonacci Number Generator
#### Problem Description
This script generates `n`-th prime Fibonacci number. A Fibonacci number is a number in the sequence where a number is the addition of the last two numbers in the sequence. A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

#### Solution
```python
def is_prime(num: int) -> bool:
    """
    Check if a number is prime.

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
    Generate the nth Fibonacci number.

    Args:
    n (int): The position of the Fibonacci number to generate.

    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.

    Args:
    n (int): The position of the prime Fibonacci number to generate.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    count = 0
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num
        i += 1


# Example usage:
if __name__ == "__main__":
    print(prime_fib(1))   # Output: 2
    print(prime_fib(2))   # Output: 3
    print(prime_fib(3))   # Output: 5
    print(prime_fib(4))   # Output: 13
    print(prime_fib(5))   # Output: 89
```
This script first defines helper functions `is_prime` to check if a number is prime and `fibonacci` to generate Fibonacci numbers. The `prime_fib` function uses these helpers to find the `n`-th prime Fibonacci number. It generates Fibonacci numbers incrementally and checks if each one is prime, stopping when it finds the `n`-th prime Fibonacci number.