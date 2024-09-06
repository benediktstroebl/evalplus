```python
def truncate_number(number: float) -> float:
    """
    Returns the decimal part of the number, by removing the largest integer less than the number.
    """
    tests pass:
    - Test case with negative numbers: -1.5 == 0.5 + Test test number with 0.5
    test case with non-integer numbers.
    """
    require: float
    - Test case with complex numbers: 1.5j == 0.5
    original number

    one.
    - Test case with non-decimal numbers.
    """
    test pass:
        - Test case with floating point numbers less than 0.
    """

def test_truncate():
    assert truncate_number(-1.5) == 0.5
   
    assert truncate_number(0.5) == 0.0
    assert truncate_number('1.5') == 0.5
    assert truncate_number('1.5j') == 0.8
```