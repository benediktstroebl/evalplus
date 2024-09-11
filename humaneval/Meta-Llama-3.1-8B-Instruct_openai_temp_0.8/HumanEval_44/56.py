```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    convertString = "0123456789"
    # Perform integer division to get quotient and remainder
    result = ""
    while x > 0:
        result = convertString[x % base] + result
        x = x // base
    return result

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input. It converts the number `x` to the specified base and returns the result as a string. The function uses a while loop to repeatedly divide the input number by the base and append the remainder to the result. The remainder is obtained by taking the modulus of the input number with the base, and the quotient is obtained by performing integer division. The `convertString` variable is used to map the remainder to a string representation of the digit in the new base.