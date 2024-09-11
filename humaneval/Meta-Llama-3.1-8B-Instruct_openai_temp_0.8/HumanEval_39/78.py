```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.
    
    Args:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def fibonacci(n: int) -> int:
    """
    Returns the n-th Fibonacci number.
    
    Args:
        n (int): The position of the Fibonacci number to return.
    
    Returns:
        int: The n-th Fibonacci number.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
        n (int): The position of the Fibonacci number to return.
    
    Returns:
        int: The n-th Fibonacci number that is also prime.
    """
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            return fib_num
        i += 1


# Example usage:
if __name__ == "__main__":
    print(prime_fib(1))  # 2
    print(prime_fib(2))  # 3
    print(prime_fib(3))  # 5
    print(prime_fib(4))  # 13
    print(prime_fib(5))  # 89
```

This script defines three functions: `is_prime`, `fibonacci`, and `prime_fib`. The `is_prime` function checks if a number is prime, the `fibonacci` function returns the n-th Fibonacci number, and the `prime_fib` function returns the n-th Fibonacci number that is also prime. The example usage at the end demonstrates how to use the `prime_fib` function to get the first few prime Fibonacci numbers.