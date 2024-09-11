```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.
    
    Args:
    num (int): The number to be checked.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci():
    """
    Generator function to yield Fibonacci numbers.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number to be found.
    
    Returns:
    int: The n-th Fibonacci number that is also a prime number.
    """
    fib = fibonacci()
    count = 0
    for num in fib:
        if is_prime(num):
            count += 1
            if count == n:
                return num


# Test cases
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script first checks if a number is prime using the `is_prime` function, and then uses a generator function to yield Fibonacci numbers. It then uses the `prime_fib` function to find the n-th Fibonacci number that is also a prime number. The test cases at the end demonstrate the function's correctness.