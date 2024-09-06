```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base"""
    if x < 0 or base < 2:
        raise ValueError("base must be > 0 and > 1")
        
    s = str(x)
    n = len(s)
    if base == 10:
        return s
    elif base == 2:
        return s[::mod(n, 2)]
    else:
        return s[::int(base ** (n - 1))]

# Example usage
x = 8  # any integer number
base = 3  # any integer number

try:
    result = change_base(x, base)
    print(result)
except ValueError as e:
    print(f"Error: {e}")

# Test cases with specific inputs and base values
test_base10 = change_base(8, 10) == '8'
test_base2 = change_base(8, 2) == '088'
test_base35 = change_base(7, 35) == '237'
test_base16 = change_base(7, 16) == '23716'
test_base_invalid = change_base(-7, 2)
```