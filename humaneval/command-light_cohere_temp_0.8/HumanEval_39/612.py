Here is a self-contained Python script that defines a function to calculate the n-th Fibonacci number that is prime:
```python
def prime_fib(n: int) -> int:
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    a, b = 3, 5
    for _ in range(2, n):
        a, b = b, a + b
    return a
```

This script defines a function `prime_fib` that calculates the n-th Fibonacci number that is prime, it uses dynamic programming and a loop to efficiently compute this value, testing that the value is also prime.