### Prime Fibonacci Numbers
#### Python Script

```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.
    
    Args:
    num (int): The number to check for primality.
    
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
    Generates the nth Fibonacci number.
    
    Args:
    n (int): The position of the Fibonacci number to generate.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]


def prime_fib(n: int) -> int:
    """
    Returns the nth number that is a Fibonacci number and it's also prime.
    
    Args:
    n (int): The position of the number to find.
    
    Returns:
    int: The nth number that is a Fibonacci number and it's also prime.
    """
    count = 0
    num = 0
    while count < n:
        num += 1
        if is_prime(fibonacci(num)):
            count += 1
    return fibonacci(num)


# Test cases
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
```

This script defines three functions:

*   `is_prime(num)`: Checks if a number is prime by iterating from 2 to the square root of the number and checking for divisibility.
*   `fibonacci(n)`: Generates the nth Fibonacci number by maintaining a list of Fibonacci numbers and appending the sum of the last two numbers in each iteration.
*   `prime_fib(n)`: Finds the nth number that is a Fibonacci number and it's also prime by incrementing a number, checking if it's a Fibonacci number and prime using the `is_prime` and `fibonacci` functions, and repeating this process until the nth number is found.

The script includes test cases to verify the correctness of the `prime_fib` function.