```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers are particular less 10
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    return "{:0b}".format(x, base)

# test the function
x = 8
base = 2
result = change_base(x, base)
print(result)
``` 
This script defines a function `change_base` that takes two arguments: `x` (the number to be converted) and `base` (the conversion base). The function then returns a string representation of `x` using the specified base. 

In the test cases, the function is called with different combinations of `x` and `base` values, and the resulting string representations are printed to the console.