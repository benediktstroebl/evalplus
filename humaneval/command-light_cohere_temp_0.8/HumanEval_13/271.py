```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs must be a positive integer")
    return max(x for x in range(1, min(a, b) + 1) if (a % x, b % x) == (0, 0))

# Test cases
test_ greatest_common_divisor(3, 5) -> 1
test_ greatest_common_divisor(25, 15) -> 5
test_ greatest_common_divisor(9, 13) -> 9
test_ greatest_common_divisor(1, 4) == 1
test_ greatest_common_divisor(56, 12) == 12
test_ greatest_common_divisor(0, 0)
```