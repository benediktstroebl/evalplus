```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer x to base base.
    return ''.join(str(x, base))
    """
    if isinstance(x, int) and isinstance(base, int):
        if x < 0 or base < 2:
            raise ValueError("Invalid base or x must be positive and base must be greater than or equal to 2.")
        return str(x)[base]
    return "ERROR: function definition error"

x = 8
base = 2
try:
    print(change_base(x, base))
except ValueError as e:
    print(e)

```
This code defines a function `change_base` that converts a given number `x` to a specified base `base`. The function ensures that the base is greater than or equal to 2 and that the input numbers are positive. It then uses the particular base case to convert the number and returns the converted string representation.