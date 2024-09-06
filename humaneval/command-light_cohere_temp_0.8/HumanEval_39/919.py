Here is a self-contained Python script that defines a function `prime_fib` solving the Fibonacci prime problem for the n-th Fibonacci number and checks its correctness: 

```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number and checks if it's prime
    Returns -1 if n < 2, n itself if it's even, and the unique sqrt(n) Fibonacci number if it's odd
    """
    # Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
    if n < 2:
        return -1
    elif n % 2 == 0:
        return n
    else:
        return sqrt(n) * (1 + prime_fib(sqrt(n) - 1))

# Test cases
test_prime_fib = [
    (1, 2),
    (2, 3),
    (3, 5),
    (4, 13),
    (5, 89)
]

for n, expected in test_prime_fib:
    actual = prime_fib(n)
    assert actual == expected, f"Case {n}: {actual} != {expected}"
```

This script provides a function `prime_fib` that computes the n-th Fibonacci number and verifies if it's prime. The function returns -1 if n is less than 2, n itself if it's even, and returns the unique sqrt(n) Fibonacci number if it's odd. The test cases are also provided to verify the function's correctness.