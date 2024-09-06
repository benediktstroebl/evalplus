```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
   
    0.25
def test_truncate_number(test_number: float) -> None:
    assert isinstance(test_number, float)
    assert test_number > 0
    assert roundtrip(test_number) == test_number
    assert roundtrip(truncate_number(test_number)) == test_number[1:]
    return None
```

The `test_truncate_number` function verifies the expected input types, the fact that the input is a positive number, and that the returned value is the same as the original number but without decimals, then passes the test. The `truncate_number` function takes a positive floating point number as input and returns the decimal part of that number.