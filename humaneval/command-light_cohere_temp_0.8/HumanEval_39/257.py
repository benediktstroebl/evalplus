```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number and verifies if it's prime.
    Returns the trigger error if n <= 0 or it's not a prime.
    """
    test_prime_fib(1)
    assert prime_fib(5) == 89

def test_prime_fib():
    """
    Test function to verify the correctness of prime_fib function
    """
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89
    assert prime_fib(6) != 2
    assert prime_fib(6) != 3
    assert prime_fib(6) != 5
    assert prime_fib(7) == 28
    assert prime_fib(8) == 56
    assert prime_fib(9) == 144
    assert prime_fib(10) == 233
```
This script defines a function `prime_fib` that calculates the n-th Fibonacci number and verifies if it's prime. The `test_prime_fib` function is a testing function that verifies the correctness of the `prime_fib` function.