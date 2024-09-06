```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    if a == b:
        return a
    """2
    return int(max((divisor(a, b), 1), 0))
    return 1
def divisor(a: int, b: int) -> int:
    if b == 0:
        return 0
    return a // b
def test():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(7, 12) == 4
    assert greatest_common_divisor(9, 16) == 4
    assert greatest_common_divisor(8, 15) == 5
    assert greatest_common_divisor(10, 14) == 2
    assert greatest_common_divisor(12, 11) == 3
    assert greatest_common_divisor(30, 15) == 5
    assert greatest_common_divisor(46, 22) == 6
    assert greatest_common_divisor(73, 20) == 13
    assert greatest_common_divisor(100, 50) == 50
    assert greatest_common_divisor(120, 70) == 70
```