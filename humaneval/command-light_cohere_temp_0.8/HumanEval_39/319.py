```python
def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and is prime.
    The solution follows the regular expression: [2, 3, 5, 13...are prime], 
    and all other numbers are not.
    The regular expression is converted to a set of numbers and all primes 
    are removed.
    Returns None if n<0.
    """
return [int]("2" if n==1 else 
    '3' if 2^(n-1) in [2,3] else 
    '5' if 3^(n-1) in [2,3] else
    '13' if 5^(n-1) in [2,3,13] else
    '89' if 13^(n-1) in [2,3,13] else None)
)
```