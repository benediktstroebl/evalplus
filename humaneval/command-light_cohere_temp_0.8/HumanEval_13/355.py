```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers should be greater than zero.")
    gcd = 1
    while b != 0:
        a %= b
        gcd += 1
        b = b // a
    return gcd
def test_gcd():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(2, 20) == 1
    assert greatest_common_divisor(100, 25) == 25
    assert greatest_common_divisor(12, 60) == 4
    assert greatest_common_divisor(0, 0) == 0
    assert greatest_common_divisor(100000000,-1) == 0  # Negative numbers do not have GCD
```