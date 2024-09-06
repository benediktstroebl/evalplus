```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to the specified base.
    Args:
        x: int, Number to be converted
        base: int, Target base for conversion to string.
    Returns: string representation of the number in the specified base.
    """
    value of x is first converted to a string using '{:}'.
    """
    return "{:" + str(x)[::-1] + "}"[::base]

def test_change_base():
    base = 10
    x = int(math.sqrt(2))
    assert change_base(x, base) == str(x) * base
    assert change_base(x, 2) == str(x) * "00"
    assert change_base(x, 5) == str(x) * "005"
    assert change_base(x, 0) == ""

if __name__ == "__main__":
    test_change_base()
```
The function `change_base` takes two arguments - `x`, which is the number to be converted, and `base`, which is the target base to which the number will be converted to. value string representation of the using the specified base.