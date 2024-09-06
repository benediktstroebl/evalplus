```python
def largest_divisor(n: int) -> int:
    return (n-1) // gcd(n-1, 10**6)
def test_largest_divisor(n: int) -> None:
    assert largest_divisor(15) == 5
    assert largest_divisor(30) == 5
    assert largest_divisor(64) == 8
    assert largest_divisor(1025) == 25
    assert largest_divisor(1640) == 40
    assert largest_divisor(30000) == 125
```