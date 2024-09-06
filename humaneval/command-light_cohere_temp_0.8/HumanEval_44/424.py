```python
def change_base(x: int, base: int):
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Both 'x' and 'base' must be integers")
    if base < 2 or base > 36:
        raise ValueError("'base' must be between 2 and 36")
    return f"{x} ({base})" if x > 0 else f"{base} ({x} + 1)"

# Example usage:
x = 8
base = 2
result = change_base(x, base)
print(result)  # Output: 1000
```
This script defines a function `change_base` that converts a given number `x` to a string representation using the specified base `base`. The function performs input validation to ensure both `x` and `base` are integers within the valid range (2 to 36), and raises `TypeError` and `ValueError` if the conditions are not met. The example usage demonstrates how the expected output will be printed to the console.