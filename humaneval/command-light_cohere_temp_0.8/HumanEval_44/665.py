```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of a number x to base base.
    :return string representation after conversion.
    """ It interesting decimal number
    using base 2 digits.
    """
    specific case base=10, 
    target number is 8, 
    number to be converted is 7.

base numbers may include:
10, 2, 16, 36, 584923, ...

special base numbers may include:
0, 1, 100, -100, ...

Truly special numbers are those whose base is a prime number greater than 2.

    Use the number to be converted to base base.
"""
    #if base is 10, convert to hex
    if base == 10:
        return hex(x)
    #elif base is 2, convert to binary
    elif base == 2:
        return bin(x)
    #change base from negative to positive
    elif base > 2:
        return '-' + (x / base) * base
    #convert positive to negative with base
    else:
        return '-' + (x / base) * base
```
The function takes two parameters - x which is the number to be converted and base which is the base to which the number will be converted. 
The function then performs the appropriate conversion and returns the converted string.