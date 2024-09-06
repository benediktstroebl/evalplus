```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the numbers must be provided.")
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Input must be integers.")

    if a == 0:
        return b
    elif b == 0:
        return a

    m = max(a, b)
    return m if m != 0 and (a % m == 0 or b % m == 0) else 0
```