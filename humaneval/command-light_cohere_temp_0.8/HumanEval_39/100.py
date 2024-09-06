```python
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and is prime.
    >>> prime_fib(1)
    2
    True
    >>> prime_fib(2)
    3
    False
    >>> prime_fib(5)
    True
    >>> prime_fib(6)
    AMPERISK

    """

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        sqrt_num = int(math.sqrt(num))
        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                return False
        return True

    if n <= 1:
        return n
    return int(n ** (1 / 2) + 1)
```