```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n exactly and is less than n.
    """
    if n <= 1:
        return n
    lcm = n // gcd(n)
    return lcm
def test_largest_divisor(n):
    assert largest_divisor(n) == n // gcd(n), f"Error: {largest_divisor} does not return {n / gcd(n)}"
    return largest_divisor(n)
```