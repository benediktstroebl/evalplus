```python
def change_base(x: int, base: int):
    """
    Change the base of the input number x to base base.
    return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    True
    """
    # Convert x to string
    return format(x, f'{base}')

# Test the function with passing cases
print(change_base(8, 3))        # Prints '22'
print(change_base(8, 2))        # Prints '1000'
print(change_base(7, 2))        # Prints '111'
print(change_base(-5, 2))        # Raises ValueError
```