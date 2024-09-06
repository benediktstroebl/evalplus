```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the numbers must be provided.")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Input must be integers.")

    if a == 0:
        return b
    elif b == 0:
        return a

    m = a
    while b != 0:
        a, b = b, a % b

    return a
```