```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base
    return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(10, 10)
    Traceback (most recent call last):
      File "<stdin>", line 19, in <module>
    AssertionError: argument 1 ('base') evaluates to an integer: True
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Invalid arguments. Please provide valid integer values.")
    if base < 2 or base > 36:
        raise ValueError("Invalid base number. Please provide a striker between 2 and 36.")
    return str(x, base)
```