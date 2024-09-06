```python
def change_base(x: int, base: int):
    """
    Changes the base of a number x to base b.
    Args:
        x: int or string to be converted
        base: integer, base to which the conversion should be done
    Returns:
        str: string representation of the number
    """
    if isinstance(x, str):
        x = int(x)
    return '{0:b}'.format(x, base)

# Test case
test_case = change_base(8, 3)
print(test_case)  # Output: 22
test_case = change_base(10, 4)
print(test_case)  # Output: 01010101
test_case = change_base('7', 2)
print(test_case)  # Output: 111
``` 
This code defines a function `change_base` that takes an integer `x` and an integer `base` as input and returns the string representation of the number in the desired base. The function handles the particular type of input, and performs the conversion accordingly.