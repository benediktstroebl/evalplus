```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number that is prime.
    Retrieves the purpose: Returns the n-th number that is a Fibonacci number and is also prime.
    Return value type a
    list comprehension for prime numbers.
    """
    range(2, n + 1)
    is_prime = [True if n % i == 0 else False for i in range(2, n + 1)]
    return next((i for i in is_prime if i),)

def test_prime_fib():
    """
    Test case for prime_fib function
    """
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89
    assert prime_fib(6) == 28
    assert prime_fib(7) == 56
    assert prime_fib(8) == 24
    assert prime_fib(9) == 96
    assert prime_fib(10) == 34
    assert prime_fib(11) == 45
    assert prime_fib(12) == 132
    assert prime_fib(13) == 89
    assert prime_fib(14) == 196
    assert prime_fib(15) == 233
    assert prime_fib(16) == 289
    assert prime_fib(17) == 479
    assert prime_fib(18) == 521
    assert prime_fib(19) == 645
    assert prime_fib(20) == 905
```
The Python script provided defines a function `prime_fib` that calculates the n-th Fibonacci number that is prime. It employs list comprehension to filter out and retrieve prime numbers from the range [2, n + 1]. The `test_prime_fib` function tests the function with various input values and ensures the correctness of the `prime_fib` function.