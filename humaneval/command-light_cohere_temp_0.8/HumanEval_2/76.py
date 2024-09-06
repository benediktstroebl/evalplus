```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> truncate_number(3.5) == 0.25
   5 number equal a dry number, the integer part is the largest integer less than 3.5, which is 3 in this case. 
    """
    dry number, the integer part is two and the decimal part is five.

    # Test cases
    dry number:
    assert truncate_number(3.5) == 0.5
    assert truncate_number(0.5) == 0
    dry number:
    assert truncate_number(5) == 1.7
    assert truncate_number(-5) == -1.6
    test to demonstrate that the function handles negative numbers correctly.
```