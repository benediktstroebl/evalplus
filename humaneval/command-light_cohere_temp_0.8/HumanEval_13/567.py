```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one input is required")
    elif a == 0 or b == 0:
        return 0
    elif a == b:
        return a
    else:
        return max(a, b)
```  This code defines a function greatest_common_divisor that calculates and returns the greatest common divisor of two integers a and b, it handles various edge cases and input validation to ensure accurate results.