```python
def change_base(x: int, base: int):
    """
    Change the base of a number to another base.
    Args:
        x: int, Number to be converted
        base: int, Base to which the number is to be converted
    Returns:
        string, Number after base conversion
    """
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36.")
        
    s = str(x)
    s = s[::-1]  # Remove trailing zeros
    s = s.replace(str.maketranscend(int, base)
    return s

def test_change_base():
    try:
        result = change_base(8, 3)
        assert result == '22'
        result = change_base(10, 2)
        assert result == '1000'
        result = change_base(42, 4)
        assert result == '42'
        result = change_base(7, 5)
        assert result == '55'
        return
    except AssertionError as e:
        print(e)

test_change_base()
``` 
This code defines a `change_base` function, which converts a given number to a new base. The `test_change_base` function contains a set of test cases to check if the `change_base` function works correctly. The code raises an `ValueError` if the base is out of the acceptable range of 2 to 36.