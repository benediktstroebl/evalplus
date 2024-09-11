```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
    x (int): The number to be converted.
    base (int): The target base.
    
    Returns:
    str: The string representation of the number in the target base.
    """
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    return ''.join(map(str, digits[::-1]))

# Test cases
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

In this script, we use a while loop to continuously divide the input number by the target base and append the remainder to the `digits` list. The remainders are the digits in the target base, and we append them in reverse order to get the correct result. Finally, we use the `join` function to concatenate the digits into a string.