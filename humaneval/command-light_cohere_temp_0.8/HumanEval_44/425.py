```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to base b.
    Parameters: x: number to be changed
    base: base to which the number will be changed
    Returns: string representation of the converted number
    """
    # Ensure base is a valid integer
    assert isinstance(base, int) and base > 0, "Invalid base number.

    # Apply conversion using the Barlier's exponentiation formula for converting to base b
    # formula: x^b = (x * ((b^(1+x)) / ((b-1)!)
    x = x ** (base - 1)
    return str(x)

# Test the function
x = 8
base = 3
result = change_base(x, base)
assert result == '22', f'The result is not {result}. Passed test!
x = 8
base = 2
result = change_base(x, base)
assert result == '1000', f'The result is not {result}. Passed test.'
x = 7
base = 2
result = change_base(x, base)
assert result == '111', f'The result is not {result}. Passed test.'
```