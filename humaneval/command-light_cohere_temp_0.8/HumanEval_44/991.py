```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of input number x to base base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    """
    return format(x, f', '.{d{base}', decimals=1)[0]
``` 
This function formats the number to the desired base using the format() string method and the format characters .d{base} (where base is the current base and d is an integer specifying the number of digits to display).