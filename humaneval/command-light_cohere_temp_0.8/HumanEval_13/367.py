```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the numbers is required")
    if a == 0:
        return 0
    elif b == 0:
        return a
    else:
        return 1
def test_gcd():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(10, 25) == 5
    assert greatest_common_divisor(40, 60) == 20
    assert greatest_common_divisor(2, 16) == 16
    assert greatest_common_divisor(16, 14) == 2
    assert greatest_common_divisor(9, 13) == 13
    assert greatest_common_divisor(49, 31) == 7
    assert greatest_common_divisor(5, 49) == 7
```