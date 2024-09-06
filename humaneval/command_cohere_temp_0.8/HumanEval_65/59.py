```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    x = str(x)
    if len(x) < shift:
        return x + x[::-1]
    return x[shift:] + x[:shift]
```

The function first converts the integer `x` to a string using `str(x)`. Then, it checks if the length of the string is less than the shift value, returning the original number concatenated with its reverse if so. This handles the edge case where the shift value is greater than the number of digits. Finally, if the shift value is acceptable, the function returns a string that results from concatenating the end of the string, shifted by `shift` positions, to the beginning of the string.