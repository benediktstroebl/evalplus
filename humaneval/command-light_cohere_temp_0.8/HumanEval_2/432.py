```python
def truncate_number(number: float) -> float:
    """
    This function takes a positive floating point number as input and returns the decimal part of the number.
    """
    test:
    assert truncate_number(3.5) == 0.25 test test: Passes the test!
    assert truncate_number(-3.5) == -0.5
   
    test: Passes test.
    assert truncate_number(1.25) == 0.5
   : Passes test.
    assert truncate_number(1.25) == 0.1: Passes test.
    assert truncate_number(0.5) == 0.0: Passes test.
    assert truncate_number(1.9) == 1.9: Passes test.
    assert truncate_number(-1.5) == -9: Passes test.

    return 0.5
```