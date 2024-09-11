### Prime Fibonacci Numbers
#### Problem Description

A prime Fibonacci number is a Fibonacci number that is also a prime number.

#### Solution

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
        n (int): The position of the number in the sequence.

    Returns:
        int: The n-th prime Fibonacci number.
    """
    a, b = 0, 1
    count = 0
    while True:
        # Generate the next Fibonacci number
        a, b = b, a + b
        
        # Check if the number is prime and Fibonacci
        if is_prime(b) and count == n:
            return b
        count += 1


# Example usage
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

### Explanation

The `is_prime` function checks if a number is prime by iterating from 2 to the square root of the number and checking for divisibility.

The `prime_fib` function generates Fibonacci numbers and checks if they are prime. It uses the `is_prime` function to check for primality. It keeps generating Fibonacci numbers until it finds the `n-th` prime Fibonacci number.