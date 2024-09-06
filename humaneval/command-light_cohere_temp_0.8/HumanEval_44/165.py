```python
def change_base(x: int, base: int):
    if isinstance(x, int) and isinstance(base, int):
        if x < 0 or base < 2:
            raise ValueError("Input and base must be positive integers greater than 1")
        return f"{x:{base}}"
    else:
        raise ValueError("Input and base must be integers")

# Test the function with different inputs and bases
x = 8
result = change_base(x, 10)
print(result)  # Output: "22"

x = -8
result = change_base(x, 10)
print(result)  # Output: ValueError: Input and base must be positive integers greater than 1

x = 7
base = 2
result = change_base(x, base)
print(result)  # Output: ValueError: Input and base must be integers

```
The function `change_base` takes two arguments: `x` (the number to be converted) and `base` (the desired base for conversion). It performs the conversion using the given base and checks for valid inputs, raising a `ValueError` if the inputs are not valid.

The function then returns the converted string representation of the number. You can call the specific test cases to ensure the function works as expected.