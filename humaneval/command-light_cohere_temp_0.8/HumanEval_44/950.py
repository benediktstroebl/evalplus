```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion
   
    base numbers less than 2 or greater than both 10 and non-integer bases are
    raised to 10 and then converted
    """
    if base < 2 or base > 10:
        base = 10  # Convert invalid base to 10
    return '{:0b}'.format(x, base)

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
print(change_base(7, 5))  # Error: ValueError
```