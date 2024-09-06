```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, n // max(n))
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
def test_largest_divisor():
    assert largest_divisor(15) == 5
    assert largest_divisor(24) == 8
    assert largest_divisor(4) == 2
    assert largest_divisor(0) == 0
    assert largest_divisor(42) == 6
    assert largest_divisor(100) == 20
```