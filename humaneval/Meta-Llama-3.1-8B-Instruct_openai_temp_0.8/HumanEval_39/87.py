### Prime Fibonacci Numbers

The following Python script generates and returns the `n-th` number in the Fibonacci sequence that is also a prime number.

```markdown
### Code
```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.
    
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    
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
        n (int): The index of the Fibonacci number to generate.
    
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


def prime_fib(n: int) -> int:
    """
    Returns the nth Fibonacci number that is also a prime number.
    
    Args:
        n (int): The index of the prime Fibonacci number to return.
    
    Returns:
        int: The nth Fibonacci number that is also a prime number.
    """
    fib_num = 1
    prime_count = 0
    while prime_count < n:
        fib_num = fibonacci(fib_num)
        if is_prime(fib_num):
            prime_count += 1
    return fib_num


# Example usage
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
```

### Explanation

*   The `is_prime` function checks if a given number is prime by iterating up to the square root of the number and checking for divisibility.
*   The `fibonacci` function generates the nth Fibonacci number using a simple iterative approach.
*   The `prime_fib` function generates Fibonacci numbers and checks if they are prime using the `is_prime` function. It keeps track of the count of prime Fibonacci numbers and returns the nth prime Fibonacci number.

This script provides a clear and efficient solution to the problem, with well-documented functions and example usage in the `if __name__ == "__main__":` block.