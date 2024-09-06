```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base
    >>> change_base(8, 10)  # 8 converted to base 10
    '88'
    >>> change_base(123, 12)  # 123 converted to base 12
    'xxx'
    >>> change_base(12345, 15)  # Powered by Python f64 support
    '1.234567'
    lost
    """
    base = 'x'  # Custom base
    original = x  # Save original number
    base_str = '{0:b}'  # Convert base to string
    new_base = int(base_str)  # Convert base string to integer
    new_x = base_str[::-1].index(base)  # Find the index of the base in the original number
    new_x += len(base_str) - 1  # Add the length of the original base
    new_x = x - new_x  # Subtract the original base from the original number
    return f"{original:b}({base_str})"  # Return the number with the new base
```