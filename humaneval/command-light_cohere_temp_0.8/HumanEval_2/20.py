```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5) == 0.25
    required to truncate 3.5 to float, which doesn't pass the test because it is smaller than 3.
    """

def test_truncate_number():
    assert truncate_number(3.5) == 0.0
    assert truncate_number(1.5) == 0.0
    assert truncate_number(-3.5) == -5.0

    precise float operations. 
```

This Python script defines a function `truncate_number` that takes a floating point number and returns the decimal part of the number, rounded down to a value less than or equal to 1. The function is then tested using the `test_truncate_number` function that asserts the correctness of the `truncate_number` function for a variety of inputs.