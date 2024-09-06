```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs cannot be zero.")
    return math.gcd(a, b)

# Unit tests
def test GreatestCommonDivisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(12, 48) == 4
    assert greatest_common_divisor(15, 75) == 15
    assert greatest_common_divisor(0, 0) == 0
    assert greatest_common_divisor(10, 110) == 10
    assert greatest_common_divisor(29, 121) == 121
    assert greatest_common_divisor(-12, -8) == 4
    assert greatest_common_divisor(21, 25) == 5
```