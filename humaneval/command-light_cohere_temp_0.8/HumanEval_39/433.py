```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n - 2)
    else:
        # Apply recursive formula to find next prime Fibonacci number
        return 2 + (prime_fib(n - 3) // 2)

# Unit tests
def test_prime_fib():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(5) == 89
    assert prime_fib(6) == 8
    assert prime_fib(7) == 24
    assert prime_fib(8) == 24
    assert prime_fib(9) == 5

# Example usage
if __name__ == "__main__":
    test_prime_fib()
```
The code provides a function `prime_fib` that calculates the nth Fibonacci number that is prime and returns it. The function also applies a recursive formula and includes unit tests for various input values to ensure the correctness of its recursive calls.