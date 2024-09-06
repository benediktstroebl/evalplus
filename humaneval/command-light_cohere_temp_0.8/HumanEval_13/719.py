```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be set")
    if a == 0 or b == 0:
        return 0
    return max([d for d in range(1, min(a, b)) if a % d == 0 and b % d == 0])
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(16, 256) == 16
    assert greatest_common_divisor(20, 3) == 5
    assert greatest_common_divisor(0, 4) == 0
```