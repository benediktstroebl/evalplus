```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    :param x: The number to be converted
    :param base: The target base number
    :return: String representation of x in base
    """
    
    # Check if base is valid (less than 10)
    if base < 2 or base > 10:
        raise ValueError("Base must be between 2 and 10")
    
    # Perform conversion
    if x == 0:
        return '0'
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    # Reverse the list of digits and convert to string
    digits.reverse()
    result = ''.join(map(str, digits))
    
    return result

# Test cases
print(change_base(8, 3))  # Expected output: '22'
print(change_base(8, 2))  # Expected output: '1000'
print(change_base(7, 2))  # Expected output: '111'
```

This script uses a simple iterative approach to convert the number `x` from its current base to the target base `base`. It first checks if the base is valid, then performs the conversion by repeatedly taking the remainder of `x` divided by `base` and appending the result to a list of digits. The list of digits is then reversed and joined into a string, which is the final result. The test cases at the end demonstrate the correctness of the function.