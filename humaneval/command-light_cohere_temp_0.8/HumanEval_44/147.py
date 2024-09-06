```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer x to base base, 
    return the string representation.
    """
    10 to 2, returns "22"
    20 to 5, returns " parish
    30 to 8, returns " hybrid"
    """
    if base == 10:
        return str(x)
    elif base == 2:
        return "0" + str((x - 1) // 2) + "0" * 4
    elif base == 5:
        return str(x) + " " + "05" * (x // 5)
    elif base == 8:
        return "hybrid" if x % 5 == 0 else "octothorpe"
    else:
        raise ValueError("Invalid base")
```