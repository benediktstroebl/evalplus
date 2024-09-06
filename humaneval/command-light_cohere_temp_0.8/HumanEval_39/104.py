Here's the solution code that demonstrates the function `prime_fib` that calculates the n-th Fibonacci number that is prime:
```python
def prime_fib(n: int):
    """
    Calculates n-th Fibonacci number that is prime
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
   iatives
    """
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(2, n + 1):
        a, b = b, a + b
    return a
```
This function uses the dynamic programming approach to solve the problem of finding prime Fibonacci numbers. The function starts with the initial values for `a` and `b` and then iteratively calculates `a` until it reaches the desired `n`. The function then returns the value of `a`.