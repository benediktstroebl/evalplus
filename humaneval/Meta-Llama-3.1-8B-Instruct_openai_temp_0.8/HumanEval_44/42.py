### Numerical Base Conversion
```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Args:
        x (int): Input number.
        base (int): Numerical base to convert to (less than 10).
    
    Returns:
        str: String representation of x in the new base.
    """
    convertString = "012345678"
    if x < base:
        return convertString[x]
    else:
        return change_base(x // base, base) + convertString[x % base]

# Example usage:
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```
This script uses a recursive function to convert the input number to the desired base. The `//` operator performs integer division and the `%` operator calculates the remainder. The `convertString` is a string containing the numerical digits in the new base.