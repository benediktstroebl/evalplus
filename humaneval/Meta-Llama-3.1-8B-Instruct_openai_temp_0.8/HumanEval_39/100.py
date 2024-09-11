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
        # Generate the next Fibonacci number
        a, b = b, a + b
        
        # Check if the new Fibonacci number is prime
        if is_prime(b):
            count += 1
            if count == n:
                return b


# Test cases
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script first defines a helper function `is_prime(num)` that checks whether a number is prime. It then defines the `prime_fib(n)` function, which generates Fibonacci numbers and checks whether each one is prime using `is_prime(num)`. The function keeps track of the count of prime Fibonacci numbers and returns the `n-th` one. Finally, it includes test cases to verify that the function works as expected.