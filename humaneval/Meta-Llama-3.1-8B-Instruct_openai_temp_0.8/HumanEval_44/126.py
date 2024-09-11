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
        digits.append(str(x % base))
        x //= base
    
    return ''.join(reversed(digits))

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script uses a while loop to continuously divide the input number `x` by the target base and append the remainder to the `digits` list. The remainders are converted to strings to handle bases greater than 10. Once the loop finishes, the list of digits is reversed and joined into a single string to form the result. If the input number is 0, the function returns '0' immediately.