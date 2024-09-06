```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to the given base.
    Args:
        x: The number to be converted
        base: The base to which the number is to be converted
    Returns:
        string representation of the converted number
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base number.
    return '{:02d'.format(x, base=base)

x = 8 # Example input number
base = 2  # Example base
result = change_base(x, base)
print(result)

# Test cases
x = 8 # Example input number
base = 10  # Example base
result = change_base(x, base)
print(result)

x = 'abc' # Example invalid input
base = 2  # Example invalid base
try:
    result = change_base(x, base)
    print(result)
except ValueError as e:
    print(e)
```
This code defines a function `change_base` that converts a given number `x` to a string representation using a specified base `base`. The base can be any valid integer between 2 and 36. The function raises a ValueError if the base is invalid. It then uses the string formatting to convert the number and returns the result. Finally, it passes test cases to the function to ensure the functionality is correct.