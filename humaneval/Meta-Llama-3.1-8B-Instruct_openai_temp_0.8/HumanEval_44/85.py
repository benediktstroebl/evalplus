```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    return ''.join(map(str, digits[::-1]))

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that converts a number `x` from base 10 to a specified base `base`. The function works recursively by repeatedly taking the remainder of `x` divided by `base` and prepending it to the result. When `x` becomes 0, the function stops and returns the result as a string. 

The test cases at the end demonstrate the function's behavior for different inputs.