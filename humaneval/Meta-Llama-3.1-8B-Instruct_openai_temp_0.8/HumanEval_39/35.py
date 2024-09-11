```python
def is_prime(num: int) -> bool:
    """
    is_prime checks if a number is prime.
    
    Args:
    num (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci(n: int) -> int:
    """
    fibonacci returns the n-th number in the Fibonacci sequence.
    
    Args:
    n (int): The position of the number in the Fibonacci sequence.
    
    Returns:
    int: The n-th number in the Fibonacci sequence.
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        for _ in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The n-th position of the prime Fibonacci number.
    
    Returns:
    int: The n-th prime Fibonacci number.
    """
    count = 0
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            count += 1
            if count == n:
                return fib_num
        i += 1


# Test the function
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```
This script first checks if a number is prime using the `is_prime` function. Then it generates Fibonacci numbers using the `fibonacci` function. The `prime_fib` function uses these helper functions to find the n-th prime Fibonacci number. It keeps generating Fibonacci numbers and checking if they are prime until it finds the n-th prime Fibonacci number.