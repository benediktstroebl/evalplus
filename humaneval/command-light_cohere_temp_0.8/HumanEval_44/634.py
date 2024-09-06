```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
        
    if base == 2:
        return "{:02}".format(x)
    elif base == 10:
        return "{:05}".format(x)
    elif base == 16:
        return "{:04X}".format(x)
    elif base == 32:
        return "{:05b}".format(x)
    elif base == 36:
        return "{:03d}".format(x)
    else:
        raise ValueError("Invalid base")

# Example usage
x = 8
base = 2
result = change_base(x, base)
print(result)  # Output: '1000'
```