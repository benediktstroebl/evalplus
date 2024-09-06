```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base base"""
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36.")
    s = str(x)
    n = len(s)
    s = s[::-1] + s[1:]  # Odd number of digits
    while s[0] == '0':
        s = s[1:]
    while s[n - 1] == '0':
        s = s[:n - 1] + s[n:]
    return s.
# Test function
 test cases
print(change_base(8, 3))      # Output: '22'
print(change_base(7, 2))       # Output: '111'
print(change_base(10, 4))      # Output: '00010'
print(change_base(1, 35))     # Output: '1'
print(change_base(0, 2))     # Output: '00'
```