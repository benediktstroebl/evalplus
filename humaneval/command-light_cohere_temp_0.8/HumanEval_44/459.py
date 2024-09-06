```python
def change_base(x: int, base: int) -> str:
    """Change the base of input number x to base base, 
    and return the string representation.
    base can be any 10 or
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(5, 1)
    Traceback (most recent call last):
      File "<stdin>", line 467: maybe a missing hint or docstring
    ValueError: 'int' object does not support item assignment assignment operator = / a = 5'
    """
    if base > 1 and base <= 36:
        return f'{x:{base}}'
    else:
        raise ValueError("Invalid base value. Base must be between 1 and 36.")
```
This Python function, change_base, takes an integer x and an integer base as input, and returns the string representation of x with the base converted. It uses the the also checks that the base is between 1 and 36, and raises an error if the base is outside this range.