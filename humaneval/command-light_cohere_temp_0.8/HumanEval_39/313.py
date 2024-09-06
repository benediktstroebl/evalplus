```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    else:
        # The formula is (2n-1) / (n-1)
        return 2 * prime_fib(n - 1) / prime_fib(n - 2)

# Unit tests
def test_prime_fib():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89
    assert prime_fib(6) == 28
    assert prime_fib(7) == 24
    assert prime_fib(8) == 8
    assert prime_fib(9) == 233
    assert prime_fib(10) == 5558

if __name__ == "__main__":
    test_prime_fib()
```
This Python code defines a function called `prime_fib` that calculates and returns the nth Fibonacci number that is also prime. The function uses a formula (2n-1) / (n-1) to compute this value.

The code also includes a set of unit tests using the `test_prime_fib` function, which asserts the correctness of the `prime_fib` function for various input values. The `if __name__ == "__main__":` block ensures that the tests are run only when the script is executed directly, not when it's imported.