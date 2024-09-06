Here's the provided Python script:
```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base value. Base must be between 2 and 36.")
    return format(x, base)
```

The function change_base takes two parameters: `x`, which is the number to be converted, and `base`, which is the base to which the number will be converted. The function then checks if the base is valid, and if not, raises a ValueError exception. If the base is valid, it returns the string representation of the number using the specified base. The base numbers are valid between 2 and 36, ensuring that the input base is within a valid range.

The function uses the built-in function `format()` that formats the number `x` using the specified base.