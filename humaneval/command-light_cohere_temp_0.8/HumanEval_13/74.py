```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the numbers is not provided.")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both numbers must be either integers or floats.")
    if a == 0 or b == 0:
        return 0
    gcd = math.gcd(a, b)
    while a != 0 or b != 0:
        a, b = b, a % b
    return gcd
def test_gcd():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
def test_type_checking():
    assert isinstance(greatest_common_divisor(3, 5), int)
    assert isinstance(greatest_common_divisor(25, 15), int)
def test_zero():
    assert greatest_common_divisor(0, 5) == 0
```