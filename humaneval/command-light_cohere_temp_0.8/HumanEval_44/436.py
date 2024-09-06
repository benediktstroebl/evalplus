```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base
    """
    return f'{x:>{base}'  # use f-string formatting for better output readability

def test_change_base():
    """
    Test the change_base function with various inputs and bases.
    assert change_base(12, 10) == '1200'
    assert change_base(123, 9) == '123_ ninth'
    assert change_base(123, 2) == '2300'
    assert change_base(10, 20) == '20__'
    assert change_base(111, 21) == '11111_ twentieth'
    assert change_base(1, 2) == '02__'
    assert change_base(12, 15) == '4806_ tenth'
    assert change_base(123, 16) == '15_ seventeenth'
    assert change_base(0, 4) == '  4096'
```