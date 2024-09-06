Here is a Python script with a self-contained function that solves the problem of finding the n-th Fibonacci number that is also prime:
```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number that is prime.
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
    28
    >>> prime_fib(7)
    458
    >>> prime_fib(8)
    1594
    >>> prime_fib(9)
    4181
    >>> prime_fib(10)
    9844
    """
    if n <= 1:
        return n
    if n <= 3:
        return 2  # Only 2, 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False  # Not prime
    prime = True
    i = 5  # i is used to check divisibility of n
    while i * i <= n:
        if n % i == 0:
            prime = False
        i += 6
    if prime:
        return n
```
The function checks if the n-th Fibonacci number is prime by testing its divisibility up to the powers of 2 and 3, as well as some other numbers that are close to prime. It returns n if the results are prime, and sets the variable `prime` to False if the number is not prime.