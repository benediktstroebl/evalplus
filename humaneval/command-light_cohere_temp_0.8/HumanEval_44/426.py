```python
def change_base(x: int, base: int) -> str:
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Input must be an integer")

    # Ensure valid base
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")

    # Perform conversion
    return format(x, f"{{base}}", int(base))

# Test cases
print(change_base(8, 3))     # Output: '22'
print(change_base(8, 2))    # Output: '1000'
print(change_base(7, 2))    # Output: '111'
print(change_base(123, 0))   # Should raise ValueError
print(change_base(-8, 2))  # Should raise ValueError
```
This Python script defines a function `change_base` that takes two arguments: `x` (the number to be converted) and `base` (the desired base for conversion). The function performs validation to ensure that `x` is an integer and that the `base` is within an acceptable range (between 2 and 36). It then uses the `format format` function to convert `x` into a string representation using the specified base. The script provides a necessary number of test cases to validate the functionality of the `change_base` function.