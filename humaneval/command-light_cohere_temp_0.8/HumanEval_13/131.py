```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("One or both inputs must be a positive integer.")

    # The GCD algorithm with recursion
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(a-1, b-1) + 1

# Unit tests
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(0, 5) == 0
    assert greatest_common_divisor(5, 0) == 0
    assert greatest_common_divisor(-5, 10) == 5
    assert greatest_common_divisor(100, 25) == 25
    assert greatest_common_divisor(75, 100) == 50
    assert greatest_common_divisor(50, 50) == 0
```