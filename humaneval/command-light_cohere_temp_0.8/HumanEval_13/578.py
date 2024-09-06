```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs must be a non-zero integer.")

    if a == 0:
        return b
    elif b == 0:
        return a

    # Find the greatest common divisor using the Euclidean algorithm
    while a != 0 and b != 0:
        a, b = b, a % b
    return max(a, b)

# Unit tests
def test GreatestCommonDivisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(6, 2) == 3
    assert greatest_common_divisor(0, 10) == 10
    assert greatest_common_divisor(15, 0) == 0
    assert greatest_common_divisor(9999, 1) == 1
    assert greatest_common_divisor(0, 0) == 0
```