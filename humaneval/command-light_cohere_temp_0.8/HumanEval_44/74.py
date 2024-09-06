Here's a self-contained Python script that defines a function `change_base` solving the problem of changing the base of a given number to a desired base:

```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to the base b.
    Convert x into a string representation.
    Ifs base numbers in base b and convert them to strings.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    return format(x, base)
```