```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    return max(gcd(a, b), 1)
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
def test_gcd():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
test_gcd()
```