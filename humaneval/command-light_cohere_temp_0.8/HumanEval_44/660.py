```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of a given number x to base base.
    Args:
        x: int, the number to be converted
        base: int, the desired base to convert to
    Returns:
        str, the converted number
    """
    if x < 0:
        raise ValueError("Input number must be positive")
    elif base <= 0 or base >= 10:
        raise ValueError("Base must be a positive integer less than 10")
        
    result = str(x)
    while result[0] == '0' and base > 0:
        result = result[1:] + str(base)
        base -= 1
    return result
```