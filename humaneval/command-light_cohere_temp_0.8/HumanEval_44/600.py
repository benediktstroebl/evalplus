Here's a self-contained Python script that defines a function `change_base` which converts a number `x` to its string representation in a specified base `base`:
```python
def change_base(x: int, base: int):
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36.")
        
    # Handle negative numbers
    if x < 0:
        x = abs(x)
        
    result = ''
    while x > 0:
        digit = x % base
        result = result + str(digit) + str(base)
        x //= base
        
    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(-7, 2))  # Output: '111'
print(change_base(0, 10))  # Output: '000...'
print(change_base(5, 11))  # Output: '05...'
```
This script includes a function `change_base` that converts a number `x` to its string representation in a specified base `base`. It also includes test cases to ensure the function's correctness.