```python
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and is also prime.
    >>> print(prime_fib(1))
    2
    Is 2 a prime number?
    True
    >>> print(prime_fib(2))
    3
    Is 3 a prime number?
    False
    ...
    >>> print(prime_fib(5))
    89
    Is 89 a prime number?
    True
    >>> print(prime_fib(6))
    True
    >>> print(prime_fib(10))
    It's undefined for 10
    """

def test_prime_fib():
    """
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(5) == 89
    assert prime_fib(6) == True
    assert prime_fib(10) == None
    assert prime_fib(21) == 2
    assert prime_fib(77) == 3  # This will cause an error
    """
```
The function test_prime_fib can be used to run the test suite, and you can add additional test cases as needed.