```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        a = prime_fib(n // 2)
        if a == 2:
            return 3
        elif a == 3:
            return n
        else:
            return_value = prime_fib(n - 1) + a * prime_fib(n - a - 1)
            return return_value

# Unit tests
def test_prime_fib():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(5) == 89
    assert prime_fib(6) == 28
    assert prime_fib(10) == 55
    assert prime_fib(12) == 497
    assert prime_fib(20) == 547
    assert prime_fib(50) == 2880
    assert prime_fib(100) == 4181
```

The above script provides a function `prime_fib` that computes the n-th Fibonacci number and returns the n-th prime number. The function handles the tested with a series of tests that cover various input values, including small numbers, squares, odd numbers, and larger values.