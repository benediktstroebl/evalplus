```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, 1)
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
def test_largest_divisor():
    assert largest_divisor(15) == 5
    assert largest_divisor(16) == 8
    assert largest_divisor(20) == 4
    assert largest_divisor(8) == 2
    assert largest_divisor(9) == 3
    assert largest_divisor(30) == 5
    assert largest_divisor(0) == 0
    assert largest_divisor(100) == 10
```