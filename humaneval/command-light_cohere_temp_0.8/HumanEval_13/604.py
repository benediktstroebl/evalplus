```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs cannot be zero")
    if a == b:
        return a
    # Calculate the GCD using the Euclidean algorithm
    while a != b:
        old = a
        a = b
        b = old % b
    return b
```