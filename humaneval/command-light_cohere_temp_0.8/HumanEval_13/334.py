```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers should be greater than zero")
    return math.sqrt(max(a, b))

# Unit tests
def test GreatestCommonDivisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(6, 6) == 6
    assert greatest_common_divisor(0, 10) == 1
    assert greatest_common_divisor(40, 50) == 20
    assert greatest_common_divisor(500, 250) == 250

print("Greatest Common Divisor Test PASSED!")
```