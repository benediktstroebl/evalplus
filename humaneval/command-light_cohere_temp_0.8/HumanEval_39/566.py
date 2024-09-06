```python
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and is prime.
    return a number, n, such that it is a Fibonacci number and greater than 2, but smaller than sqrt(n^2)
    """
    if n < 2:
        return n
    if n < 3:
        return 3  # already prime
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        n += i
    return True

def test_prime_fibonacci(num:
    """
    assert prime_fibonacci(num)
    pass
```
The function `prime_fibonacci` calculates and returns the n-th Fibonacci number that is prime, if n is a positive integer. 

The function first checks if n is less than 2, and returns n if so. It then checks if n is 2 or greater and returns `False` if so, as 2 and greater numbers are not prime. It then starts a test for divisibility, and returns `True` if n is not divisible by any integer less than or equal to the square root of n^2.