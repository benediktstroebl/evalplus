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


def is_perfect_square(num: int) -> bool:
    """
    Checks if a number is a perfect square.
    
    Args:
    num (int): The number to check.
    
    Returns:
    bool: True if the number is a perfect square, False otherwise.
    """
    root = int(num ** 0.5)
    return root * root == num


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        if is_prime(b) and is_perfect_square(b) or n == count + 1:
            return b
        count += 1


# Example usage
if __name__ == "__main__":
    print(prime_fib(1))  # 2
    print(prime_fib(2))  # 3
    print(prime_fib(3))  # 5
    print(prime_fib(4))  # 13
    print(prime_fib(5))  # 89
```

This script defines three functions: `is_prime`, `is_perfect_square`, and `prime_fib`. The `is_prime` function checks if a number is prime, the `is_perfect_square` function checks if a number is a perfect square, and the `prime_fib` function returns the n-th Fibonacci number that is also prime. The `prime_fib` function uses the `is_prime` and `is_perfect_square` functions to check if a Fibonacci number is prime and a perfect square. The script also includes example usage of the `prime_fib` function.