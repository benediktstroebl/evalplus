```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of a number x to base base.
    Args:
        x: The number to be converted
        base: The base to convert to.Fo the number.
    Returns: string representation of the number with the specified base.
    Returns: The string representation after conversion.
    """
    number = x  # convert x to a number
    string = str(number)  # convert to string using built-in function
    return string  # return the string representation of the number

# test the function
print(change_base(8, 3))  # expected output: 22
print(change_base(10, 3)) # expected output: 110
print(change_base(10, 2)) # expected output: 1000
print(change_base(10, 5)) # expected output: 250
```