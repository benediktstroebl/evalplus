```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs must be a positive integer")
    return max((i) for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0)

# Unit tests
def test GreatestCommonDivisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(-5) == 5
    assert greatest_common_divisor(0, 7) == 1
    assert greatest_common_divisor(1000, 500) == 500
```