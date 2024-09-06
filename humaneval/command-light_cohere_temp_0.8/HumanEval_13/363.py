Here's a self-contained Python function that calculates and returns the greatest common divisor of two integers a and b:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs cannot be zero.")
    return math.gcd(a, b)
```
Do you need assistance with anything else?