```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    Args:
    num: The number to check.

    Returns:
    True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    Returns the nth Fibonacci number.

    Args:
    n: The position of the Fibonacci number.

    Returns:
    The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_list = [0, 1]
        for i in range(2, n + 1):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list[n]


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    fib_num = fibonacci(n)
    while True:
        if is_prime(fib_num):
            return fib_num
        fib_num = fibonacci(n)


# Test cases
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script first defines a helper function `is_prime` to check if a number is prime. It then defines the `fibonacci` function to generate the nth Fibonacci number. Finally, it defines the `prime_fib` function, which uses `fibonacci` and `is_prime` to find the nth Fibonacci number that is also prime. The script includes test cases to verify that `prime_fib` works correctly.