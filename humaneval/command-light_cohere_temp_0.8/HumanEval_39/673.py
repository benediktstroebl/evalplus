```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number and is also prime.
    Returns None if n < 0
    """
    if n <= 0:
        return None
    
    # Recursive approach
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return next(fib)

# Test cases
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
assert prime_fib(6) is None # Should return None
assert prime_fib(10) == 55
```