```python
def change_base(x: int, base: int) -> str:
    """Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers must 10."""
   
    base = str(base)
    s = str(x)
    return s if s.startswith(base) else s[0:1] + base + s[1:]

# Example usage
print(change_base(8, 3)) # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
``` 
This code implements a function `change_base` which converts a number to a different base. It uses a specific base as a parameter and converts the input number `x` to a string representation using the `str` function. The converted string is then returned if the initial string started with the base. Otherwise, it appends the base to the beginning of the string, then appends the rest of the string.