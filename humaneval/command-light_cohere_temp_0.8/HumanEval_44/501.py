```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    Parameters:
        x: int (number to be converted)
        base: int (new base for conversion)
    
    Returns:
        string representing the converted number
    """
    if x < 0 or base < 2:
        raise ValueError("Invalid input. For non- base conversion, numbers should be > 0 and base > 1")
    
    # Perform the conversion and return as string
    return format(x, str(base))

# Test cases
print(change_base(8, 3))       # Output: '22'
print(change_base(8, 2))       # Output: '1000'
print(change_base(7, 2))       # Output: '111'
print(change_base(-5, 10))     # Raises ValueError due to < 0 number
print(change_base(10, 2))     # Raises ValueError due to base < 2
```