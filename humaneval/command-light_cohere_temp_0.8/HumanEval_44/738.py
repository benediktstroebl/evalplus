Here's the code you requested:
```python
def change_base(x: int, base: int):
    """
    Convert a number to a string representation using specified base.
    Parameters:
    x: int, number to be converted
    base: int, base for string representation
    Returns: str, string representation of x using base
    """
    # Define a char array of the required length
    c = [chr(i) for i in range(base+1)]
    # Initialize result as zero
    res = ''
    for i in range(x):
        res = c[i % base] + res
    return res
```
This code defines a function called `change_base` that converts a given number `x` to a string representation using a specified base. It creates a process by creating a character array to represent the digits of the base (in this case, base 10). Then, it iterates through the number `x` and appends each digit to the result string, shifted by the modulus of its index divided by the base. Finally, it returns the string representation of the number.