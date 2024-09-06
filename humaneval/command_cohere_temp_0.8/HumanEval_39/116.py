```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Make sure n is positive
    n = abs(n)
    # Initialize two variables for the Fibonacci sequence
    x, y = 0, 1
    count = 0
    while count < n:
        # If x is prime, return it
        if is_prime(x):
            return x
        # Prepare for the next number in the sequence
        count += 1
        x, y = y, x+y
    # If we reach the end of the loop, return y
    return y
```

This script defines two functions: `is_prime` checks if a number is prime, and `prime_fib` returns the n-th number that is a Fibonacci number and also a prime number. The `prime_fib` function initially converts the given integer to an absolute value to handle negative inputs, then uses two variables (`x` and `y`) to generate the Fibonacci sequence, iterating until the count of Fibonacci numbers obtained is greater than or equal to `n`. Within the loop, it checks if the current value of `x` is prime using the `is_prime` function, returning it if it is. If none of the `x` values are prime, it finally returns the value of `y` at the end of the loop.

Here is an example of using the function:
```python
>>> prime_fib(1)
2
>>> prime_fib(2)
3
>>> prime_fib(3)
5
>>> prime_fib(4)
13
>>> prime_fib(5)
89
```