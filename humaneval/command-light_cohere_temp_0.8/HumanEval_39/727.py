```python
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and is also prime.
    >>> prime_fib(1)
    2
    True
    >>> prime_fib(2)
    3
    False
    >>> prime_fib(3)
    5
    True
    >>> prime_fib(4)
    13
    True
    >>> prime_fib(5)
    89
    True
    """
    return (n <= 1) or (n == 2 and prime_fib(3)) or (n == 5 and prime_fib(4) and prime_fib(3))
```
This function, `prime_fib`, returns the n-th Fibonacci number that is prime. The function uses a nested if statements to check if the number is less than 1, or equal to 2 and 3, and if so it returns False. Otherwise, it checks if the number is equal to 5 and 4, and if so it checks if it's also prime using the `prime_fib` function.