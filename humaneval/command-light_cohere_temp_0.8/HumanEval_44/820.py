```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to base base.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(1, 10)
    Traceback (most recent call last):
      File "<stdin>", line 836, in <module>
    AssertionError: 1 != 10
    """
    if x < 0 or x == 10:
        raise ValueError("Input should be a valid number")

    original = str(x)
    new_base = [str(i) for i in str(x) if i != '0' and i != '9']

    new_base = ''.join(new_base)
    new_num = ''.join(new_base)

    return new_num
```