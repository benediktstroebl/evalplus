```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Incompatible inputs: Both numbers must be greater than zero.")

    if a == 0 or b == 0:
        return 0

    # Use the Euclidean algorithm to find the greatest common divisor
    while a != 0 and b != 0:
        a, b = b, a % b

    return max(a, b)

# Unit tests
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(0, 5) == 0
    assert greatest_common_divisor(7, 0) == 0
    assert greatest_common_divisor(5, 0) == 0
    assert greatest_common_divisor(10, -3) == 5
    assert greatest_common_divisor(-45, 10) == 45
```