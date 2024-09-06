```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """

    # Testing
    assert truncate_number(3.5) == 0.25

   05

    assert truncate_number(1) == 0
    assert truncate_number(-1) == -1
    assert truncate_number(-5) == -5
    assert truncate_number(10) == 5
    assert truncate_number(12.3) == 5.2
   1

```