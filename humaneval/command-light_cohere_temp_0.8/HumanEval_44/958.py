```python
def change_base(x: int, base: int):
    """Change the numerical base of input number x to base base.
    Convert the base numbers 10 and returns a string representation of x.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(9, 5)
    Traceback (most recent call last):
      File "<stdin>", line 31, in <module>
        File "<stdin>", line 6, in change_base
          File "<ipython.py:__main__.py>", line 26, in <module>
        File "<ipython.py:__main__.py>", line 24, in <module>
    ZeroDivisionError: division by zero
    """
    if base == 10:
        return str(x)
    return str(x).join(int(base) ** (1.0 / (x -float(x) / int(base))))
```