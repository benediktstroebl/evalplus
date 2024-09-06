```python
def change_base(x: int, base: int) -> str:
    """
    Convert a number to a string representation using a specified base.
    Args:
        x: int, number to convert
        base: int, base to use during conversion
    Returns:
        str: string representation of x in the specified base
    """
    # Ensure base is smaller than or equal to 36
    if base > 36:
        raise ValueError("Base must be smaller than or equal to 36")
        
    # Use built-in int() to ensure base will be an integer
    base = int(base)
    
    # Special case for 0 as it is represented in base 10 (decimal)
    if x == 0:
        return '0'
    
    # Use list comprehension to convert digits to strings in the given base
    digits = list(map(lambda y: format(y, base), list(x))))
    
    # Use str.join() to convert list of digits to a single string
    return str(digits)
``` 
This code defines a function `change_base` that converts an integer `x` to a string representation using a specified base `base`. The base is checked to ensure it's within the valid range of base numbers (1-36) and if it's greater, a ValueError is raised. 
The function then converts each digit in the number `x` to a string in the specified base using the `map` function. It then uses `str()` to convert the list of digit strings back to a single string.