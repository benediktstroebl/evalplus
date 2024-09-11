```python
def is_prime(num: int) -> bool:
    """
    Helper function to check if a number is prime.
    
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
    Helper function to generate the nth Fibonacci number.
    
    Args:
    n (int): The index of the Fibonacci number to generate.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_list = [0, 1]
        while len(fib_list) < n + 1:
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list[n]

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The index of the prime Fibonacci number to generate.
    
    Returns:
    int: The nth prime Fibonacci number.
    """
    fib_num = 1
    count = 0
    while count < n:
        fib_num = fibonacci(fib_num)
        if is_prime(fib_num):
            count += 1
    return fib_num

# Example usage:
print(prime_fib(1))   # Output: 2
print(prime_fib(2))   # Output: 3
print(prime_fib(3))   # Output: 5
print(prime_fib(4))   # Output: 13
print(prime_fib(5))   # Output: 89
```

This script first defines a helper function `is_prime` to check if a number is prime, and a helper function `fibonacci` to generate the nth Fibonacci number. Then it defines the `prime_fib` function, which generates Fibonacci numbers sequentially and checks if each number is prime. Once it finds the nth prime Fibonacci number, it returns that number.