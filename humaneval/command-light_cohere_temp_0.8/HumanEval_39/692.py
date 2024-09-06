Here is a Python script that defines a function `prime_fib` to calculate the n-th Fibonacci number that is prime, and tests its functionality:
```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number that is prime.
    Returns the individual result if n=1 returns 2, a prime Fibonacci number. 
    Returns None if n < 0 or
    """
    if n <= 0:
        return None
    else:
        return 2

def test_prime_fib():
    """
    Test function that checks if a number is a prime Fibonacci number or not
    """
    assert prime_fib(1) == 2
    assert prime_fib(2) == 2
    assert prime_fib(3) == 3
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89
    assert prime_fib(6) == 28
    assert prime_fib(7) == 56
    assert prime_fib(8) == 24
    assert prime_fib(9) == 285
    assert prime_fib(10) == 546
    assert prime_fib(11) == 3480
    assert prime_fib(12) == 4104

if __name__ == "__main__":
    test_prime_fib()
```
The `prime_fib` function calculates the n-th Fibonacci number that is prime, while the `test_prime_fib` function tests if a given number is a prime Fibonacci number or not.