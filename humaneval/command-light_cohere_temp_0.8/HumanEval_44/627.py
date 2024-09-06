```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the number to the given base.
    Args:
        x: int, the number to be converted
        base: int, the base to convert to
    Returns: 
        string representation of the converted number
    """
    # initialize the converted number
    s = str(x)
    # remove any non-base characters from the number
    s = s.replace(str.maketransverse(str.maketransitive))
    make sure on the radix of base
    return s

#test cases
assertEqual(change_base(8, 3), '22')
assertEqual(change_base(8, 2), '1000')
assertEqual(change_base(7, 2), '111')
```