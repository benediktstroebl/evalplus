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


def fibonacci(n: int):
    """
    Generates the nth Fibonacci number.

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
        return fibonacci(n-1) + fibonacci(n-2)


def prime_fib(n: int):
    """
    Returns the nth number that is a Fibonacci number and it's also prime.

    Args:
        n (int): The position of the number to return.

    Returns:
        int: The nth number that is a Fibonacci number and it's also prime.
    """
    num = 1
    while True:
        fib_num = fibonacci(num)
        if is_prime(fib_num):
            if n == 1:
                return fib_num
            n -= 1
        num += 1


if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

This script defines three functions:

*   `is_prime(num):` checks if a number is prime.
*   `fibonacci(n):` generates the nth Fibonacci number.
*   `prime_fib(n):` returns the nth number that is a Fibonacci number and it's also prime.

The `is_prime(num)` function checks if a number is prime by iterating from 2 to the square root of the number and checking for divisibility. The `fibonacci(n)` function generates the nth Fibonacci number using recursive function calls. The `prime_fib(n)` function uses a while loop to generate Fibonacci numbers and checks if they are prime using the `is_prime(num)` function. It returns the nth Fibonacci number that is prime.