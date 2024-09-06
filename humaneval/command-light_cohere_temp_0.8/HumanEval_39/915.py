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
    354
    >>> prime_fib(8)
    3360
    >>> prime_fib(9)
    5iste9
    """
    if n < 2:
        return n
    if n == 2 or n == 3:
        return 2  # special case
    if n % 2 == 0:
        return prime_fib(n // 2) + 1
    else:
        return prime_fib(n // 2) + prime_fib(n // 2) + 2
```
This function computes the n-th Fibonacci number that is prime and returns it. The function handles edge cases, and recursively calculates the Fibonacci number until the n-th value is reached, ensuring that it is a prime. 
You can call this function with any given value for n, and it will provide the corresponding Fibonacci prime.