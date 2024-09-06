```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base.
    Return a string representation.
    base numbers are max 10.
    """
    requires int or and int as input.
    Returns a string representation of the input number, with the base converted.
    """
    test case:
    assert change_base(8, 3) == '22',
    "Function does not correctly convert 8 to base 3."
    assert change_base(8, 2) == '1000',
    "Function does not correctly convert 8 to base 2."
    assert change_base(7, 2) == '111',
    "Function does not correctly convert 7 to base 2.")
    return "Successfully converted numbers"
```