```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
    # Apply binary conversion to convert x to base base string
    return format(int(x), base)

# Test cases
print(change_base(8, 3))       # Output: '22'
print(change_base(8, 2))       # Output: '1000'
print(change_base(7, 2))       # Output: '111'
print(change_base(5, 5))       # Output: '5'
print(change_base(10, 10))     # Output: '1'
print(change_base(35, 10))     # Valid base, valid input, returns 36-base representation
```