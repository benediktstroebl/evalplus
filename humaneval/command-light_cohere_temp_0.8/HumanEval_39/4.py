```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        # Calculate Fibonacci numbers using recursive approach
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

# Test the function with various inputs
assert(prime_fib(1) == 2)
assert(prime_fib(2) == 3)
assert(prime_fib(3) == 5)
assert(prime_fib(4) == 13)
assert(prime_fib(5) == 89)
assert(prime_fib(6) == 22)
assert(prime_fib(7) == 8)
assert(prime_fib(8) == 24)
assert(prime_fib(9) == 5)
assert(prime_fib(10) == 233)

# Test for edge cases (non-integer inputs)
try:
    assert prime_fib('a') == 2
except ValueError:
    pass  # Error: ValueError for non-integer input

print("All tests passed!")
```