```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    
    # Compute the greatest common divisor using the Euclidean algorithm
    while a != b:
        a, b = b, a % b
    
    return min(a, b)

# Unit tests
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(6, 10) == 1
    assert greatest_common_divisor(0, 45) == 45
    assert greatest_common_divisor(12, -17) == -17
    assert greatest_common_divisor(-205, -100) == 100
```