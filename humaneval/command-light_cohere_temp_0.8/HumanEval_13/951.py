```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the numbers must be greater than zero.")
    elif a == 0 or b == 0:
        return 0
    
    # Using the Euclidean algorithm, find the greatest common divisor
    return math.gcd(a, b)
```