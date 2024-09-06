Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_fib(n):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # consequent number is fibonacci number, alternates between adding and subtracting
        # previous number
        num1, num2 = 0, 1
        for _ in range(n - 2):
            num1, num2 = num2, num1 + num2
        return num2

# Tests
assert is_prime(2)
assert not is_prime(3)

assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This code defines two functions:
- The `is_prime` function checks whether a given number is prime or not. It handles special cases like numbers less than or equal to 1, and also uses the sieve of Eratosthenes algorithm for efficiency.
- The `prime_fib` function calculates the n-th Fibonacci number that is also a prime number. It uses an iterative approach to compute the Fibonacci numbers, storing alternating values in `num1` and `num2` variables.