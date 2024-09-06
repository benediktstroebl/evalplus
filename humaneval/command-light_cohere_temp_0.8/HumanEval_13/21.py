```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one input is zero.")
    return math.gcd(a, b)

def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
```