```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 1
    if n % 3 == 0:
        return 5
    for i in range(5, n + 1):
        if n % i == 0:
            return i
    return 0  # not a Fibonacci number or not prime

# Test suite

def test_prime_fib():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89
    assert prime_fib(6) == 2
    assert prime_fib(7) == 3
    assert prime_fib(8) == 5
    assert prime_fib(9) == 8
    assert prime_fib(10) == 13
    assert prime_fib(11) == 12
    assert prime_fib(12) == 23
    assert prime_fib(13) == 8
    assert prime_fib(14) == 17
    assert prime_fib(15) == 25
    assert prime_fib(16) == 16
    assert prime_fib(17) == 49
    assert prime_fib(18) == 16
    assert prime_fib(19) == 33
    assert prime_fib(20) == 5
```
This script defines a function `prime_fib` that calculates and returns the n-th Fibonacci number, which is also a prime. The test suite includes various test cases to verify the function's correctness.