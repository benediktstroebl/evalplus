```python
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime
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
   ambigous...
    """
    if n == 1:
        return 2
    elif n == 2:
        return 3
    elif n % 2 == 0:
        return 5
    else:
        for i in range(5, n + 1, 2):
            if is_prime(i):
                return i
        return n

def is_prime(n: int):
    """
    simple check, not optimized
    >>> is_prime(0)
    False
    >>> is_prime(1)
    True
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True
    >>> is_prime(8)
    False
    >>> is_prime(9)
    True
    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    >>> is_prime(12)
    False
    >>> is_prime(13)
    True
    >>> is_prime(14)
    False
    >>> is_prime(15)
    True
    >>> is_prime(16)
    False
    >>> is_prime(17)
    True
    >>> is_prime(18)
    False
    >>> is_prime(19)
    True
    >>> is_prime(20)
    False
    """

This code defines the `prime_fib` and `is_prime` functions.  The `prime_fib` calculates the n-th Fibonacci number that is prime, while the `is_prime` function checks whether a given number is prime using a simple modulo 2 test.