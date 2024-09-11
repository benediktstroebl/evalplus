Here is a Python script that uses a helper function to generate Fibonacci numbers and another function to check for primality:
```markdown
### Fibonacci and Prime Numbers
#### Returning the n-th Fibonacci number that is also prime

```python
def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    
    Args:
        n (int): The index of the Fibonacci number to return (starting from 1).
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


# Example usage
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89
```

This script defines two helper functions: `is_prime` checks if a number is prime, and `prime_fib` generates Fibonacci numbers until it finds the `n-th` prime one. The `prime_fib` function uses a loop to generate Fibonacci numbers and checks each one for primality using the `is_prime` function. The first Fibonacci number that is also prime is returned after the specified number of iterations.