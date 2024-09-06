```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be not equal to or zero.")

    if a == 0 or b == 0:
        return 0

    return max(a, b) / math.is_integer(min(a, b))

```
Do you need assistance with anything else?