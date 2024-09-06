```python
def largest_divisor(n: int) -> int:
    return next(
        i for i in range(1, n+1) if any(d % i == 0 for d in range(1, i)))
def test__largest_divisor():
    assert largest_divisor(15) == 5
    assert largest_divisor(20) == 4
    assert largest_divisor(12) == 4
    assert largest_divisor(24) == 6
    assert largest_divisor(28) == 28
    assert largest_divisor(50) == 50
```