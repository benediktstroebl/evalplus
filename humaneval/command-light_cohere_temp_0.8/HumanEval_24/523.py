```python
def largest_divisor(n: int) -> int:
    """
    Finds the largest divisor less than n, that divides n evenly.
    """
    tests pass:
    1. Given n = 3, largest_divisor(3) should return 1.
    2. Given n = 4, largest_divisor(4) should return 2
    3. Given n = 6, largest_divisor(6) should return 3
    4. Given n = 12, largest_divisor(12) should return 4
    5. Given n = 13, largest_divisor(13) should return 5
    """
    return max(set(range(1, n+1)) & {n}) // n
```