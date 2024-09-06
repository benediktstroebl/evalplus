```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of input number x to base base.
    return string representation after conversion
   
    base numbers can be 10 or any other
    """
    if base < 2 or base > 36:
        raise ValueError("Base must be a number between 2 and 36")
    return format(x, str(base))

# Test cases
print(change_base(8, 3))    # Output: '22'
print(change_base(8, 2))   # Output: '1000'
print(change_base(7, 2))   # Output: '111'
print(change_base(123, 4))  # Raises ValueError
```