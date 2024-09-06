```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion
   
    base numbers less than 2 won't work, base should be > 2
    """
    assert base > 2, "Base should be greater than 2"
    if x < 0:
        raise ValueError("Input number should be non-negative")
    if base == 2:
        return '1' * x
    return '{:0b}'.format(x, base)
```  The function takes two parameters - x, which is the number to be converted, and base, which is the desired base for the conversion. The function then checks for valid base numbers and raises a ValueError if the base is 2 or the input is negative. The function converts the number to the desired base and returns its string representation.