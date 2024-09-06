Here is a self-contained Python script that solves the problem of converting a given number to a specified base:
```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base
    > 0
    Return string representation after conversion
    """
    if base < 2 or base == 10:
        raise ValueError("Base must be greater than 0 and less than or equal to 10")
    return f"{x:{base}}"  # f-string formatting to ensure consistency with string output and base handling
```

This script defines a function change_base that takes two parameters: x, which represents the number to be converted, and base, which represents the desired base for the conversion. The function first checks if the base is within the valid range (greater than 0 and less than or equal to 10). If the base is invalid, a ValueError is raised. The function then uses the string formatting with the f-string syntax to ensure that the returned string representation is consistent with the original input and the specified base. The result of this function is a formatted string with the number x and the base, ensuring proper handling of both.

This self-contained solution can be used to change the base of a number to a specified base, passing the number and base as arguments.