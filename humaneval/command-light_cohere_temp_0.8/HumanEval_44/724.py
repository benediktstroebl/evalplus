```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base
    """
    #handle negative numbers
    if x < 0:
        x = abs(x)
    if base == 2:
        return str(x)[::-1] + str(x)[::-1]
    else:
        return hex(x)[2:] + hex(x)[2:]
```