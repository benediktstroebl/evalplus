```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to the given base.
    Args:
        x: int, number to be converted
        base: int, base to which the conversion will be performed
    Returns: 
        str: string representation of x in the new base
    """
    assert isinstance(x, int) and x >= 0, "Input must be a non-negative integer"
    assert isinstance(base, int) and base >= 2 and base <= 36, "Base must be a positive integer between 2 and 36"

    # First, determine length of x as a decimal string
    x_len = len("%.{ _{x}__)
    # Convert x to the desired base, and concatenate to a string
    base_converted = [""] * (x_len // base) + ["".join(base_len % base) for base_len in (x_len % base, 0, base_len)]

    return base_converted[0]
```