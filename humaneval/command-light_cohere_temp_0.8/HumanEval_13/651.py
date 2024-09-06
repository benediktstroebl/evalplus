```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    
    a, b = max(a, b), min(a, b)
    return (a + b) // gcd(a, b)

# Unit tests
def test GreatestCommonDivisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(6, 60) == 60
    assert greatest_common_divisor(90, 25) == 5
    assert greatest_common_divisor(0, 10) == 0
    assert greatest_common_divisor(100, 50) == 50
```