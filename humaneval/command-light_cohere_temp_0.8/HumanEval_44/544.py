```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers are smaller than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(123, 1)
    Traceback (most recent call last):
      File "<input>", line 11, in <module>
    AssertionError: cannot convert int to string: 123
    """

    # convert number to string
    string = str(x)

    # convert string to corresponding base
    result = [int(x[i:i+base]) for i in range(len(string))]

    return result

```