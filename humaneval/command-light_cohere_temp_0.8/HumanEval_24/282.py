```python
def largest_divisor(n: int) -> int:
    """
    Return the largest integer divisor of n that is less than n itself.
    """
    example usage:
    n = 31
    print(largest_divisor(n))  # Output: 5
    assert largest_divisor(n) >= 1
    assert largest_divisor(n) <= n
    assert largest_divisor(30) == 5
    assert largest_divisor(27) == 9
    return n // 2 + 1
```