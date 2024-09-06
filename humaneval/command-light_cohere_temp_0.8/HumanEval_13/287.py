```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("Both numbers must be non-zero.")
    if not a % b == 0 or not b % a == 0:
        raise ValueError("Both numbers must be relatively prime.")
    return abs(a - b) // gcd(a, b)

# Unit tests
def test GreatestCommonDivisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(125, 19) == 5
    assert greatest_common_divisor(56, 72) == 8
    assert greatest_common_divisor(111, 99) == 9
    assert greatest_common_divisor(37, 13) == 2
    assert greatest_common_divisor(49, 14) == 2
    assert greatest_common_divisor(19, 51) == 19
```