Here's a Python script that defines a function, `prime_fib` solving the Fibonacci number problem for the n-th Fibonacci number that is also prime:

```python
def is_prime(n):
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
    Returns the n-th Fibonacci number that is prime.
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
    >>> prime_fib(6)
    2468
    """
    if n <= 1:
        return n
    if n <= 3:
        return True
    if is_prime(n) == False:
        return False
    return prime_fib(n + 1)
```

The function `is_prime` checks whether a given number is prime or not. The function uses a `if...else` statement to check conditions for divisibility and then uses the `i` loop to check divisibility up to the square root of the given number. 

The function then returns the value of `prime_fib` if the given number is prime and otherwise returns `False`.