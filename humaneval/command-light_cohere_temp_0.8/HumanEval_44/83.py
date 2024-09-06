```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to the specified base.
    :return "<base>"_str(x, base)
    """
    return f"{base}_{str(x, base)}"

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
print(change_base(10, 5))  # Error: invalid base, should raise ValueError
```