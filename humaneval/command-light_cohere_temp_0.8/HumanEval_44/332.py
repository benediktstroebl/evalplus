```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to the given base.
    Args:
        x: int, the number to be converted
        base: int, the base to convert to
    Returns:
        str: string representation of the converted number
    """
    assert isinstance(x, int) and base > 0, "Invalid base value.
    result = bin(x)[2:]
    return result.make_string(result, base)
```
This code defines a function change_base that takes an integer x and an integer base as input, and returns the string representation of the number converted to the specified base. The code uses the specific test assertions to ensure that the base is greater than 0 and that the input is an integer. 
This function follows the principles of binary conversion to decimal numbers and uses the make_string() method to correctly convert the binary representation of the number to a string.