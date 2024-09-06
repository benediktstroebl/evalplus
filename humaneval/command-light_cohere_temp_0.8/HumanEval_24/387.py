```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, n - 2)

def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b%a, a)

# Unit tests
def test_largest_divisor():
    assert largest_divisor(1) == 1
    assert largest_divisor(2) == 2
    assert largest_divisor(3) == 3
    assert largest_divisor(4) == 4
    assert largest_divisor(5) == 5
    assert largest_divisor(10) == 5
    assert largest_divisor(15) == 5
    assert largest_divisor(20) == 4
```