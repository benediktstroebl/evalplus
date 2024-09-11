```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    convertString = "0123456789ABCDEF"
    if x < base:
        return convertString[x]
    else:
        return change_base(x // base, base) + convertString[x % base]

# Test cases
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
print(change_base(10, 2))  # Output: 1010
print(change_base(16, 16))  # Output: 10
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input. The function uses recursion to convert the number `x` to the desired base. The `convertString` variable is used to map the digits 0-9 and A-F to their string representations.

The script also includes test cases to demonstrate the function's correctness.