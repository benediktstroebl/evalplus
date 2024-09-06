```python
def largest_divisor(n: int) -> int:
    return (n-1) // gcd(n-1)
def gcd(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y
    return x
def test_largest_divisor():
    assert largest_divisor(15) == 5
    assert largest_divisor(20) == 4
    assert largest_divisor(0) == 0
    assert largest_divisor(-1) == -1
    assert largest_divisor(21) == 7
```