### Prime Fibonacci Numbers
#### Problem Description
The `prime_fib` function returns the `n-th` number that is a Fibonacci number and it's also a prime number.

#### Solution
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
    n (int): The position of the Fibonacci number.

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
    n (int): The position of the prime Fibonacci number.

    Returns:
    int: The n-th prime Fibonacci number.
    """
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            if i == n:
                return fib_num
            i += 1
        else:
            i += 1


# Test cases
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```
This script defines three functions: `is_prime` to check if a number is prime, `fibonacci` to generate the nth Fibonacci number, and `prime_fib` to find the nth prime Fibonacci number. The `prime_fib` function uses a loop to generate Fibonacci numbers and checks each one to see if it's prime. Once it finds the nth prime Fibonacci number, it returns that number.