```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of a number to another base, 
    and returns the string representation.
    Args: 
        - x (Integer): The number to be changed 
        - base (Integer): The base to which the number will be converted
    Returns: 
        - str: The string representation of the converted number
    """
    if x < 0 or base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    return str(format(x, base))
```