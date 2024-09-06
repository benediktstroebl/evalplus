```python
def change_base(x: int, base: int):
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Both x and base should be integers.")
    if base < 2 or base > 36:
        raise ValueError("Base should be between 2 and 36.")
    # Perform the conversion
    result = str(x)
    while base > 1:
        result = result[0:result.length // ord(result[1]) + base
        base //= base
    return result
```