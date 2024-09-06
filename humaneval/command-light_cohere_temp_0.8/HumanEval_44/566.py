```python
def change_base(x: int, base: int):
    """
    Change the base of the number x to the specified base.
    Args: 
        - x (int): number to be converted 
        - base (int): desired base for conversion
    Returns: 
        str: converted number 
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base. Use base between 2 to 10, 36")
    return format(x, base)

#Test the function with a basic conversion to base 10
print(change_base(8, 10))
# Prints '22'

#Test the function with valid bases
print(change_base(8, 2))
# Prints '1000'
print(change_base(7, 2))
# Prints '111'

# Test the function with an invalid base
try:
    print(change_base(8, 5))
except ValueError as e:
    print(e)
```