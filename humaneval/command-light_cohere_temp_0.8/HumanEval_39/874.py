```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number and checks if it's prime.

    Fibonacci numbers are prime numbers.

    1, 2, 3, 5, 8, 13, ... are factors of the sequence.

    Test cases:
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
        ?
        >>> prime_fib(7)
        ?
        >>> prime_fib(8)
        ?

    """
    if n <= 1:
        return n
    elif n <= 3:
        return 5
    elif n % 2 == 0:
        return 8
    else:
        return 13
```