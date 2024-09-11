Here's the solution to the problem in a self-contained Python script.

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
        x, remainder = divmod(x, base)
        digits.append(str(remainder))
    
    return ''.join(reversed(digits))


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines the `change_base` function which takes an integer `x` and a base number as input. It then converts `x` to the specified base and returns it as a string. The script uses the `divmod` function to perform integer division and obtain the remainder. It keeps doing this until `x` becomes 0. The remainders are stored in a list in reverse order and then joined together to form the final string representation.