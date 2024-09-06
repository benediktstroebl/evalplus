```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to base b.
    Test if the document, return the number in a string format.
    """
    return '{0' * ('0' * x) / ('1' * base) ** (x / base)
```