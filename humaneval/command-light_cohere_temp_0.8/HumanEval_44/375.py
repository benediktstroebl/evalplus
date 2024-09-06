```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to the specified base.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(1, 5)
    Trace exception: TypeError: unsupported operand type(1) in '!=': int()
    """
    try:
        if x < 0 or base < 0:
            raise ValueError("Base and number should be positive")
        return str(x)
    except ValueError as e:
        print(f"Error: {e}")
    return str(x)
```