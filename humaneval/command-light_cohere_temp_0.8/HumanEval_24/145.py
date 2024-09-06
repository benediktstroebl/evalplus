```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1,  0)
def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b, a % b)
# Unit tests
def test_largest_divisor():
    assert largest_divisor(0) == 0
    assert largest_divisor(1) == 1
    assert largest_divisor(5) == 5
    assert largest_divisor(10) == 5
    assert largest_divisor(15) == 5
    assert largest_divisor(16) == 8
    assert largest_divisor(24) == 8
    assert largest_divisor(120) == 4
    assert largest_divisor(156) == 4
    assert largest_divisor(720) == 4
test_largest_divisor()
```