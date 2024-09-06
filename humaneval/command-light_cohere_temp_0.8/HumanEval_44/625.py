```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to base base.
    Return the string representation after conversion.
    base numbers either 10 or experiment.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base('abc123', 10)
    Traceback (most recent call last):
      File "<stdin>", line 25, in <module>
        File "<string>.format>", line 6, in **`__format__`**
          File "<string>.format>", line 3, in **`__main__()`"</string>.
          File "<string>.format", line 4, in **`__main__()`"</string>:
          'format' not found in operand
    BaseError: invalid literal for argument 'format' in 'format()'
    """
    return format(x, '{:{}'.format(base))
```