```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        # Return the n-th Fibonacci number
        return fibonacci(n) + fibonacci(n-1)

def fibonacci(n: int):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Unit tests
def test_prime_fib():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(5) == 89

    assert prime_fib(6) == 55
    assert prime_fib(8) == 144

    with pytest.circle(num_tests=100):
        for i in range(100):
            assert prime_fib(i) == i
```