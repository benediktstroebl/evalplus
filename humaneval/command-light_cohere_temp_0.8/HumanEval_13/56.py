```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the numbers must be provided.")
    while a != 1 or b != 1:
        if a % b == 0:
            return b
        a, b = b, a + a
    return
def test():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(7, -3) == 3
    assert greatest_common_divisor(0, 10) == 0
    assert greatest_common_divisor(15, 25) == 5
    assert greatest_common_divisor(10, -5) == -5
```