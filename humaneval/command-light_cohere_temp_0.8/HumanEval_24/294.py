```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n evenly and is less than n.
    """
    takes advantage of the math. floor, and returns the worst number that is divisible by n and is smaller than n.
    """
    tests:
    assert math.ceil(n) <= n
   assert n % 1 == 0
    assert math.floor(n / 2) == n // 2
    assert n == 1 or (n % 3 == 0) and n > 2
    assert n == 2 or (n % 5 == 0) and n > 3
    assert n == 3 or (n % 8 == 0) and n > 6
    assert n == 4 or (n % 10 == 0) and n > 7
    assert n == 5 or (n % 13 == 0) and n > 10
    assert n == 6 or (n % 16 == 0) and n > 11
    assert n == 7 or (n % 25 == 0) and n > 14
    assert n == 8 or (n % 32 == 0) and n > 15

    return n
```