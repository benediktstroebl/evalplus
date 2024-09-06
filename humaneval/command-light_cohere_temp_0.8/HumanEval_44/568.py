```python
def change_base(x: int, base: int) -> str:
    """Change the base 10 representation of the input number x to base base."""
    # Convert to string to ensure positive integer conversion
    num = str(x)

    # Use the int() function to convert to integer and remove non-numeric characters
    num = int(''.join(filter(str.isalnumerator(char),num)))

    # Perform the conversion based on the base
    if base == 10:
        return '{0' + num[::-1] + '}'
    elif base == 2:
        return '{0' + num[0] + '}'
    else:
        # Raise an error for an invalid base
        raise ValueError("Invalid base provided")

# Test cases
print(change_base(8, 3))       # Expected output: '22'
print(change_base(8, 2))       # Expected output: '1000'
print(change_base(7, 2))       # Expected output: '111'
print(change_base(123, 5))      # Expected output: '056523'
print(change_base(-5, 10))     # Expected output: '5'
print(change_base(123, 0))     # Expected output: Error: ValueError: Invalid base provided: 0
```