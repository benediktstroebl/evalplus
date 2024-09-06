```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    return string representation.
    """
    specified base of 10, and should raise error for other bases.
    """
    string x_str_base = str(x)
    base_str = '0123456789abcdefABCDEFGHIJKLMNOPQRSTUVXYZ'
    return f"{base_str[base]}{x_str_base}"

print(change_base(8, 2)) # Output: '1000'
print(change_base(5, 2))  # Output: '111'
print(change_base(3, 1))  # Raises error
print(change_base(10, 5))  # Raises error
```