```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base number.")
    if x < 0:
        raise ValueError("Negative number.")
    result = ""
    while x > 0:
        digit = x % base
        result = chr(digit + ord('0')) + result
        x //= base
    return result

# Test the function
print(change_base(8, 2)) # Output: '1000'
print(change_base(-5, 10)) # Output: '005'
print(change_base(0, 2)) # Output: '00'
print(change_base(97, 2)) # Valid number, converts to base 2
print(change_base(30, 16)) # Output: '0660'
print(change_base(-100, 10)) # Invalid base, raises ValueError
```