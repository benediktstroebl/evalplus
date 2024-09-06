```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to the specified base.
    Return the string representation in the desired base.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36.")
    return format(x, f"{base} base")

# Example usage
x = 8
base = 2
result = change_base(x, base)
print(result)  # Output: '1000'
``` 
This function takes an integer `x` and an integer `base` as input, and returns the string representation of `x` in the specified base. 
The function first checks if the `base` is within an acceptable range, and raises a `ValueError` exception if it is not. It then uses the string formatting to convert `x` to its string representation in the desired base.