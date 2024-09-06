```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer x to base base.
    :return string representation after conversion
    """
    base numbers can be 10 or any other number
    """
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36.")
        
    # convert integer to string
    return format(x, f"{base}")

# Test cases
print(change_base(8, 3))        # Output: '22'
print(change_base(8, 2))        # Output: '1000'
print(change_base(7, 2))        # Output: '111'
print(change_base(123, 10))     # Output: '1123'
print(change_base(10, 5))       # Base 5, invalid input
print(change_base(7, 5))       # Base 5, invalid input
print(change_base(-123, 2))   # Input is negative, invalid input
```