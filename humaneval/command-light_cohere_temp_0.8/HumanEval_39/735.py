```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        if is_prime(a):
            a, b = next(a)
    c = a + b
    d = a * b
    return c if is_prime(c) else d

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
        return False
    return True

# Test suite
def test_prime_fib():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89
```
The function `prime_fib` calculates the n-th prime number in a Fibonacci sequence that is also prime, and the function `is_prime` checks whether a given number is prime or not.  The test suite includes tests to validate the correctness of these functions.