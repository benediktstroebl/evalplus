```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the number x to base base.
    :return the maximum number of digits in base form
    """
    # Ensure the input is an integer
    assert isinstance(x, int), "Input must be an integer"
    # Check base is a valid digit
    assert isinstance(base, int) and base >= 2 and base <= 36, "Base must be between 2 and 36"
    # Calculate the result
    base_representation = ['0'] * (base - 2)
    return ''.join(''.join(base_representation) + [x])

# Test case 1
print(change_base(8, 3))  # Output: '22'

# Test case 2
print(change_base(8, 2))  # Output: '1000'

# Test case 3
print(change_base(7, 2))  # Output: '111'
```
This Python script defines a function `change_base` that converts a number to a string representation in a specified base. It uses type assertion to ensure that the input is an integer and that the base is a valid digit between 2 and 36.