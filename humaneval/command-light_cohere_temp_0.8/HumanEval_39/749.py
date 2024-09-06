```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    return prime_fib(n - 1)

# Test suite to check the function's correctness
def test_prime_fib():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89
    assert prime_fib(6) == 2
    assert prime_fib(7) == 7
    assert prime_fib(8) == 24
    assert prime_fib(9) == 45
    assert prime_fib(10) == 120
    assert prime_fib(11) == 34
    assert prime_fib(12) == 169
    assert prime_fib(13) == 8
    assert prime_fib(14) == 23
    assert prime_fib(15) == 34
    assert prime_fib(16) == 512
    assert prime_fib(17) == 289
    assert prime_fib(18) == 479
    assert prime_fib(19) == 1279
    assert prime_fib(20) == 720

# Run the test suite to verify the function's correctness
test_prime_fib()
```