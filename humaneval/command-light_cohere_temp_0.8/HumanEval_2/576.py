```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    # Test case
    test
    Here is a simple test case. 
    assert truncate_number(3.5) == 0.2
    test output: True 

    # Test another case
    assert truncate_number(1.5) == 0.3
```