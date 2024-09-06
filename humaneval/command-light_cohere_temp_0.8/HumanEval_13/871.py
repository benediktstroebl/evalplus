```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be set")
    return math.max(a, b)
```
Here's a Python script with a self-contained function that calculates the greatest common divisor of two integers a and b, using the max function to compare their absolute values.