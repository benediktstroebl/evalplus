```python
def change_base(x: int, base: int):
    """
    Change the base of a number to another base
    :param x: number to be converted
    :param base: conversion base
    :return: string representation in the specified base
    """
    if x < 0 or base <= 0:
        raise ValueError("Invalid input values.
    base_str = str(base)
    return format(x, base_str)

# Example usage
x = 8
base = 2
try:
    print(change_base(x, base))
except ValueError as e:
    print(e)
```