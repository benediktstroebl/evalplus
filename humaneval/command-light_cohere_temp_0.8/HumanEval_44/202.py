```python
def change_base(x: int, base: int):
    """
    Change the base of the numerical representation of input number x to base base.
    Return string representation after conversion.
    base numbers other 10.
    """
    need to be changed to use int, not float.
    """
    print(f"{base <->int}")
    assert x > 0, "Error: Input number is negative"
    assert base != 0, "Error: Base is zero"
    assert isinstance(x, int), "Error: Input is not an integer"
    assert isinstance(base, int), "Error: Base is not an integer"
    return str(x)
```