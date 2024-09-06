```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number 'x' to the specified 'base'.
    :return string representation after base conversion
    :param x: int - the number to be converted
    :param base: int - base to which the number is converted
    :return: str - string representation of x in the base
    """
    if x < 0:
        x = abs(x)
    return "{:b}".format(x, base)
```
This function takes two parameters: x, which is the number to be converted, and base, which is the base to which the number will be converted. The function then uses the string formatting with the :b syntax to format the number in the desired base. It returns the string representation of the number in the specified base.