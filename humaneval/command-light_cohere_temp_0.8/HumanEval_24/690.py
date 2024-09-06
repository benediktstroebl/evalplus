```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)

# Test case 1
assert largest_divisor(15) == 5

# Test case 2
assert largest_divisor(2**20) == 2**20

# Test case 3
assert largest_divisor(-5) == -5
```