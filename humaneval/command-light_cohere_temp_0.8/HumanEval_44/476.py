```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of a number x to base b.
    Returns a string representation after conversion.
    """

    following rules:
    - Numbers greater than 'base' will be kept as it.
    - Numbers smaller than base will be raised to power base to get the result.
    """ e.g. 2 -> 7 -> standard case is x as 100, and 2 != 10 are converted to 10^3.
    """
    number = (x // base) * base**x
    return f'{number: {number < 10} ? int(number) : str(number)}'
    return str(number)

# Example
x = 8
base = 3
result = change_base(x, base)
print(result)  # Output: '22'

x = 8
base = 2
result = change_base(x, base)
print(result)  # Output: '1000'

x = 7
base = 2
result = change_base(x, base)
print(result)  # Output: '111'
```