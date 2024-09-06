```python
def change_base(x: int, base: int):
    """
    Changes the base of a number to another.
    Args:
        x: int, Number to be converted
        base: int, New base for conversion.
    Returns:
        string representation of the number in the specified base.
    """
    example:
    >>> change_base(8, 3)
    '22'
    """
    return '{:b}'.format(x, base)

# Unit test
test_change_base = [
    ['Given number 8 and base 3, expected '22',
     'passing test'],

    ['Given number 7 and base 2, expected '111',
     'passing test'],

    ['Given string "122" and base 10, expected '1220',
     'passing test'],

    ['Given string "111" and base 2, expected '1000',
     'passing test']
]

for test in test_change_base:
    assert change_base(*test) == test[0]
```