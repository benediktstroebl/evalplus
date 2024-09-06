```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the given number x to base b.
    >>> change_base(12321, 10) == '111221'
    >>> change_base(12321, 2) == '2321'
    >>> change_base(12321, 3) == '12321'
    >>> change_base(12321, 11) == '111221'
    >>> change_base(12321, 16) == '1216'
    >>> change_base(12321, 41) == '352321'
    >>> change_base(12321, 60) == '01736269'
    >>> change_base(10, 10) == '10'
    >>> change_base(10, 20) == '20'
    """
    return f'{x:b}'  # use float built-in function to get binary representation
```