```python
def prime_fib(n: int):
    """
    This function returns the n-th number that is a Fibonacci number and is also prime.
    Returns an error for the
    Following conditions to be satisfied:
    1 < n <= 20
    n is a Fibonacci number
    2 <= 2^(n-1)
    3 < sqrt(2^n-2) <= 2^(n-1)
    """
    assert 1 < n <= 20, "n should be less than 20"
    assert 2 <= 2 ** n - 1
    assert 3 < sqrt(2 ** n - 2) <= 2 ** n - 1
    assert n % 2 == 0
    assert n in [3, 5, 7, 11, 13, 17, 19, 23]
    return n
```