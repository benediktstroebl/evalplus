```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers 10 ors often 2 or 16.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base('abc123', 3)
    Traceback (most recent call last):
      File "<stdin>", line 467: <attribute '__dict__' mentioned but missing from 'str' object>
    """
    raise ValueError("unsupported base value")

# Example usage:
x = 8
base = 2
try:
    result = change_base(x, base)
    print(result)
except ValueError as e:
    print("Error:", str(e))
```