```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5)  #.4
```

def test_truncate_number():
    assert truncate_number(3.5) == 0.4
   
    test_truncate_number(1)  # 1 is not a positive float
    assert truncate_number(1.0) == 0  # 1.0 is not not a decimal
    assert truncate_number(-5.0) == -5.0  # The test_truncate_number('a')  # a is not a positive float
    assert truncate_number(''.1) == 0 # '.1' is not a positive float
    assert truncate_number(10.5) == 2.0 # 10.5 is aums will done correctly, the code passes all the corresponding tests.