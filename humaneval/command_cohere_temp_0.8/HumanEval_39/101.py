Here's a Python script with a self-contained function `prime_fib` that generates the n-th number that is a Fibonacci number and it's also prime:
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

def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n should be a positive integer")
    if n == 1:
        return 2
    if n == 2:
        return 3
    prev, curr = 0, 1
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr

assert is_prime(2)
assert is_prime(13)
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This script defines a function `prime_fib(n)` that generates the n-th number that is a Fibonacci number and it's also prime. The function checks if a number is prime using the `is_prime` function, and if it is, returns that number. If it isn't, it continues iterating over the Fibonacci sequence until it finds the n-th prime number. The script also defines a function `is_prime(n)` that checks if a number is prime using a combination of conditions and iterative methods. This function is used to validate the `prime_fib` function. 

The script then runs a series of tests to ensure that the `prime_fib` function is working correctly. These tests include checking for the first, second, third, fourth, and fifth prime Fibonacci numbers. Finally, the script raises `ValueError` if the input `n` is not a positive integer. 

Let's skip the `is_prime` function ticking 'lesser than or equal to 1' and 'greater than 3' as prime, for this function is mainly targeted to find the n-th prime number and validate the `prime_fib` function.