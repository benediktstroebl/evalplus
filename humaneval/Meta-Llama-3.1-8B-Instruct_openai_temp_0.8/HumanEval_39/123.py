### Prime Fibonacci Sequence
#### A Python script to find the nth number that is both a Fibonacci number and a prime number.

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
    Generates the nth Fibonacci number.
    
    Args:
        n (int): The index of the Fibonacci number to generate.
    
    Returns:
        int: The nth Fibonacci number.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def prime_fib(n: int) -> int:
    """
    Returns the nth number that is a Fibonacci number and it's also prime.
    
    Args:
        n (int): The index of the number to find.
    
    Returns:
        int: The nth number that is both a Fibonacci number and a prime number.
    """
    i = 1
    while True:
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            if i == n:
                return fib_num
        i += 1


# Test the function
if __name__ == "__main__":
    for i in range(1, 6):
        print(f"prime_fib({i}) = {prime_fib(i)}")
```

This script uses three functions:

- `is_prime(num)`: Checks if a number is prime by iterating through all numbers up to its square root.
- `fibonacci(n)`: Generates the nth Fibonacci number by using a loop to calculate the next number in the sequence.
- `prime_fib(n)`: Finds the nth number that is both a Fibonacci number and a prime number by generating Fibonacci numbers and checking if they are prime.

The `prime_fib(n)` function uses a loop to generate Fibonacci numbers and checks if each number is prime using the `is_prime(num)` function. When it finds the nth prime Fibonacci number, it returns that number.

The script then tests the `prime_fib(n)` function by printing the first 5 numbers in the prime Fibonacci sequence.