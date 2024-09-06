```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be greater than zero.")
    while b != 0:
        if a % b == 0:
            a, b = b, a // b
        else:
            break
    return a
```