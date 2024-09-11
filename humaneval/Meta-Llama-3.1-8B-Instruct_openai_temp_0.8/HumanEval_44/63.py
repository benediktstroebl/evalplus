```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    # Initialize an empty string to store the result
    result = ""
    
    # Continue the process until x is 0
    while x > 0:
        # Get the remainder of x divided by base
        remainder = x % base
        
        # Prepend the digit to the result (as a string)
        result = str(remainder) + result
        
        # Update x to be the quotient of x divided by base
        x = x // base
    
    # Return the result
    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as arguments. It converts the number `x` to the base `base`, and returns the result as a string. The function uses a while loop to repeatedly divide `x` by `base`, appending the remainder to the result string each time. The final result is the string representation of `x` in base `base`. The test cases at the end demonstrate the usage of the function.