```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to the specified base.
    Base must be a string representation of numbers, like '2' or '10'.
    """
    assert isinstance(x, str)
    assert x.isdigit()
    singularity and base,
    assert x.isdigit() in base
   
    assert x == int(x, base)
    return x  # This is a string since we're returning a character, not a number.

x = '8'
print(change_base(x, 3)) # Output: '22'
print(change_base(x, 2)) # Output: '1000'
print(change_base(x, 10)) # Output: '8'
print(change_base('A', 10)) # Error: can't convert a string to a number in base 10
print(change_base(7, 2)) # Error: input is not a string
```