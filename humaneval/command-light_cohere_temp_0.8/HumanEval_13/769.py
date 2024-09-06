```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be greater than zero")
    return math.sqrt(max(a, b))
 
# unit tests
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(2, 5) == 5
    assert greatest_common_divisor(6, 20) == 4
    assert greatest_common_divisor(10, 35) == 5
    assert greatest_common_divisor(55, 12) == 3
    assert greatest_common_divisor(0, 4) == 4
    assert greatest_common_divisor(20, 0) == 0
    assert greatest_common_divisor(-11, 44) == 11
```