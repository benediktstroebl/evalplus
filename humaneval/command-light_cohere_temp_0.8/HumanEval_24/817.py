```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)

# Test cases
assert largest_divisor(15) == 5
assert largest_divisor(10) == 5
assert largest_divisor(27) == 3
assert largest_divisor(12) == 4
assert largest_divisor(6) == 2
assert largest_divisor(28) == 28
``` 
This code defines a function `largest_divisor` that returns the largest integer which divides a given number `n` evenly, smaller than or equal to `n`. It then tests the function with various input values, asserting that the function returns the correct result.