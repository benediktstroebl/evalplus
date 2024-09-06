```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Return a string representation after conversion.
    base numbers less 10
   
    example, base can be 2 (binary), 3 (decimal), etc)
    """
    return format(x, base)

# Unit tests
def test_change_base():
    assert change_base(8, 3) == '22'
    assert change_base(5, 2) == '1000'
    assert change_base(123, 1) == '1'
    assert change_base(5, 0) == '' # Zero is empty string
    assert change_base(-5, 5) == '5'

# Run the function and tests
test_change_base()
```