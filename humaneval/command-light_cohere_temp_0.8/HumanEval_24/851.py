```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number divisible by n, smaller than n."""
    return (n + 1) // gcd(n + 1, n)

# Test the function
assertEqual(largest_divisor(15), 5)
assertEqual(largest_divisor(20, precision=10), 4)
```