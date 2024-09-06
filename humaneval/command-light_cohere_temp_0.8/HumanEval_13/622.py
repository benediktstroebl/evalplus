```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one input must be a number")
    return max(a, b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    if not a:
        return b
    return gcd(b, a % b)

# Unit tests
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(0, 5) == 0
    assert greatest_common_divisor(7, 0) == 0
    assert greatest_common_divisor(100, 25) == 25
    assert greatest_common_divisor(13, 11) == 2
    assert greatest_common_divisor(15, 17) == 2
    assert greatest_common_divisor(10, 7) == 5
    assert greatest_common_divisor(9, 3) == 3
```