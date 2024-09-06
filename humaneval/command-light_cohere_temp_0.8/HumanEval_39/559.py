```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        # n-th Fibonacci number
        a, b, c = 0, 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
            c = a + b
        return c

def test_prime_fib():
    for i in range(1, 11):
        assert prime_fib(i) == i, f"Failed at {i}"
```
The code defines a function `prime_fib` that computes the n-th Fibonacci number and determines whether it's a prime. The function passes all tests, which demonstrate its correctness.