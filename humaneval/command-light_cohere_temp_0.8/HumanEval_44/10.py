```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    """
    if base > x:
        base = x  # Prevent base from being greater than input
    if base < 2:
        base = 10  # Set base to a reasonable default
    return format(x, f"{base}d")

# Test the function with a series of inputs and base cases
for i in range(10):
    for base in range(2, 11):
        assert change_base(i, base) == str(i)
```
The provided Python code defines a function `change_base` that converts a number to a specified base. It also has a test cases using various inputs and base values to validate the correctness of the conversion. The function ensures that the base is never greater than the input number, and it defaults the base to 10 if it's less than 2.