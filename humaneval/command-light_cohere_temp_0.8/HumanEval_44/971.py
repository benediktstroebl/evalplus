```python
def change_base(x: int, base: int) -> str:
    """
    Convert number to string using specified base.
    Returns 10 digits per base, 2 is default
    """
    if base == 2:
        return '{0:0b}'.format(x)
    elif base > 2 and base <= 36:
        return '{0:0b}'.format(x, base - 2)
    else:
        raise ValueError('Invalid base number')

# Unit tests
test_change_base = []
test_change_base.py=' [
    for i in range(10):
        test_change_base.append(str(i).str(). dir(str(change_base(i, 10))))

test_change_base.py = ['.join("It should return a string representation of number with base 10, 2 is default", 5))

test_change_base.py = ['.join("It should return a string representation of number with base 2", 3))

test_change_base.py = [].join("It should return a string representation of number with base < 10, using base - 2", 7)

test_change_base.py = [].join("It should raise ValueError for invalid base number", 41)
```