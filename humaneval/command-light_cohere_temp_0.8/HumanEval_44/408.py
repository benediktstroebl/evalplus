Here's the code:
```python
def change_base(x, base):
    """Change numerical base of input number x to base.
    if type(base) == 'scientific':
        return '{:>{}'
    elif type(base) == int and base > 0:
        return '{:.2f}'.format(x, base)
    else:
        raise ValueError("Invalid base")

# Unit tests
def test_change_base():
    base = 2
    x = 8
    assert change_base(x, base) == '22.0'

def test_positive_base():
    base = 3
    x = 7
    assert change_base(x, base) == '111.0'

def test_invalid_base():
    base = 'abc'
    x = 8
    with pytest.raises(ValueError):
        change_base(x, base)
```
This code defines a function `change_base` that converts a given number `x` to a specified base `base`. It uses base conversion rules for the scientific notation, and raises a `ValueError` for invalid bases. The `test_change_base` function tests the `change_base` function with various inputs and bases. 

The `test_positive_base` function tests a positive integer base case, where the output should be rounded to two decimal places.