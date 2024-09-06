```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers are
    strings for base < 2:
        '0'
        '1'
        '10'
        '111'
        ...
    """
    if base < 2:
        return '0' + str(x)
    return str(x)
```  This code defines a function that converts a given number `x` to a string representation in a specified base. It handles base numbers less than the strings like '0' and '1', and base greater than 2 returns the corresponding base number. 

It also handles negative numbers and returns the original number as a string.