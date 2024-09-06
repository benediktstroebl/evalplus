```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers should be greater than zero.")
    if b == 1:
        return a
    elif a == 1:
        return b
    else:
        return greatest_common_divisor(a - 1, b) + 1

# Unit tests
def test GreatestCommonDivisor():
    try:
        assert greatest_common_divisor(3, 5) == 1
        assert greatest_common_divisor(25, 15) == 5
        assert greatest_common_divisor(2, 17) == 5
        assert greatest_common_divisor(10, 5) == 5
        assert greatest_common_divisor(0, 20) == 0
    except AssertionError as e:
        print(f"Failed assertion: {e}")
        raise

test GreatestCommonDivisor()
```