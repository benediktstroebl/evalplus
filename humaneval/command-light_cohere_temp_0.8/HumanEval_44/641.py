```python
def change_base(x: int, base: int):
    """
    Change the base numerical representation of the input number to base base.
    Return the string representation of the number.
    base numbers less 10.
    >>> change_base(8, 3) == '22'
    """
    return '{:0>{base}'.format(x)

def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(10, 2) == '1000'
    assert change_base(7, 2) == '111'

# Usage example
test_change_base()
```