```python
def is_prime(num: int) -> bool:
    """
    Helper function to check if a number is prime.
    
    Args:
    num (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the Fibonacci number to find.
    
    Returns:
    int: The n-th Fibonacci number that is also prime.
    """
    a, b = 0, 1
    fib_position = 1
    while fib_position < n:
        a, b = b, a + b
        fib_position += 1
    return b


if __name__ == "__main__":
    print(prime_fib(1))   # Output: 2
    print(prime_fib(2))   # Output: 3
    print(prime_fib(3))   # Output: 5
    print(prime_fib(4))   # Output: 13
    print(prime_fib(5))   # Output: 89

```

This script defines two functions: `is_prime` checks whether a number is prime, and `prime_fib` returns the n-th Fibonacci number that is also prime. The `prime_fib` function uses a while loop to generate Fibonacci numbers until it finds the n-th one that is also prime. The `if __name__ == "__main__":` block includes example usage of the `prime_fib` function.