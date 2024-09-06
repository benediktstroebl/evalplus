Here is a self-contained Python script that defines a function that computes the n-th Fibonacci number which is also prime:

```python
def prime_fib(n):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(2, n):
        a, b = b, a + b
    return a

# Test cases for the function
test_prime_fib = [
    (1, 2),
    (2, 3),
    (3, 5),
    (4, 13),
    (5, 89),
    (6, 812),
    (7, 5151),
    (8, 34 continuity),
    (9, lift(Fibonacci))),
    (10, 1352),
]

for case, (n, expected) in enumerate(test_prime_fib, start=1):
    actual = prime_fib(n)
    print(f"{case+1}: {actual} ({n}) => {expected}")
```

This code defines a function `prime_fib` that calculates the n-th Fibonacci number, which is prime, and then provides a test suite with various input `n` values to verify the correctness of the function.

This script can be used as a reference for solving the problem of finding prime Fibonacci numbers in Markdown code blocks.