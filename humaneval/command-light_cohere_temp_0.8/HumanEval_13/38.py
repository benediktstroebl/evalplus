Here is a self-contained Python function that solves the problem of finding the greatest common divisor of two integers `a` and `b`:

```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a // b) if a % b == 0 else b

# Unit tests
def test GreatestCommonDivisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(10, 15) == 5
    assert greatest_common_divisor(67, 25) == 5
    assert greatest_common_divisor(2, 3) == 1
    assert greatest_common_divisor(13, 44) == 13
```

This function uses the approach of dividing the larger number by the smaller one, and then returning the latter. This is approach ensures the smallest possible number to be returned, as the greatest common divisor of any pair of integers is the smallest number divisible by both.