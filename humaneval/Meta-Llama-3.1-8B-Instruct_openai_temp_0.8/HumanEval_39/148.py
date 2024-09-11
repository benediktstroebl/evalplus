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
    Returns the n-th Fibonacci number.
    
    Args:
    n (int): The index of the Fibonacci number.
    
    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 1:
        return n
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The index of the number.
    
    Returns:
    int: The n-th number that is a Fibonacci number and it's also prime.
    """
    fib_num = 0
    idx = 1
    while idx <= n:
        fib_num = fibonacci(idx)
        if is_prime(fib_num):
            idx += 1
        return fib_num


# Example usage:
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

This script first checks if a number is prime using the `is_prime` function, then generates Fibonacci numbers using the `fibonacci` function, and finally finds the n-th Fibonacci number that is also prime using the `prime_fib` function. The example usage at the end prints the first five numbers that are Fibonacci numbers and also prime.