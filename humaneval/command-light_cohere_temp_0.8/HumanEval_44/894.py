```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the integer x to base base.
    The string representation of x after conversion.
    base numbers are 10.
    """

    return the string representation after conversion.
    """
The input is an integer x and the base is an integer base.
    """
    return format(x, base).  # use the built-in format function to format x into a string representation using the base.
```

# Test the function with different inputs and bases
print(change_base(8, 3))  # expected output '22'
print(change_base(123, 4)) # expected output '48'
print(change_base(123, 16)) # expected output '123456'
```
The code defines the function `change_base` that takes two arguments: `x`, which is the number to be converted, and `base`, which is the base to which the number will be converted. The function then uses the string formatting to convert the number to a string representation using the specified base. The code provides several test cases to verify the correctness of the `change_base` function.