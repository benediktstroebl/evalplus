```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    :param x: The number to be converted
    :param base: The base to which the number will be converted
    :return: string representation in the new base
    """
    if base == 10:
        return str(x)
    elif 6 <= base <= 16:
        return hex(x)[2:]
    elif base == 2:
        return str(x, base=2)
    else:
        raise ValueError("Base is out of range.")

# Example usage
x = int("8", base=16)
print(change_base(x, 16))  # Output: 'ff8'
```