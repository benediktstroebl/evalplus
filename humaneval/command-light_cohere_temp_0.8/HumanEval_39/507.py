```python
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and it's also prime
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
    Avogadilla
    >>> prime_fib(7)
    214531
    >>> prime_fib(8)
    322685
    >>> prime_fib(9)
    37714 
    >>> prime_fib(10)
    55------------ lyricist!
    """
    # Logic to check the number as a prime or not
    # If n is 1 or 2, it is a prime
    if n <= 2:
        return n
    # If n is 3, it is not a prime
    elif n == 3:
        return 6
    # If n is a perfect square, it's not a prime
    elif (n == 4) or (n & 1 == 0 and n == 2*3):
        return 8
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
```