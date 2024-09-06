```python
def largest_divisor(n: int) -> int:
    return n // max(n, 1)

# Test the function
assertEqual(largest_divisor(15), 5)
assertEqual(largest_divisor(64), 1)
assertEqual(largest_divisor(10), 1)
assertEqual(largest_divisor(28), 2)
assertEqual(largest_divisor(2), 1)
```