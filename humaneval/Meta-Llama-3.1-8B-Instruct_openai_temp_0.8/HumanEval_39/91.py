```python
def is_prime(num: int) -> bool:
    """
    is_prime checks if a number is prime.
    
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
    fibonacci returns the nth Fibonacci number.
    
    Args:
    n (int): The position of the Fibonacci number to return.
    
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


def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number to return.
    
    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            if i == n:
                return fib_num
        i += 1


# Test the function
print(prime_fib(1))   # 2
print(prime_fib(2))   # 3
print(prime_fib(3))   # 5
print(prime_fib(4))   # 13
print(prime_fib(5))   # 89
```

This script defines three functions: `is_prime`, `fibonacci`, and `prime_fib`. The `is_prime` function checks if a number is prime, the `fibonacci` function returns the nth Fibonacci number, and the `prime_fib` function returns the nth number that is both a Fibonacci number and prime. The script then tests the `prime_fib` function with the provided test cases.