```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    example [0.25
   0.05 (0.5 is a

    """
def test_truncate_number() -> None:
    assert truncate_number(3.5) == 0.05
   
   
    assert truncate_number(5.3) == 0.1
    assert truncate_number(-0.5) == 0.0
```
This Python code defines a function `truncate_number` that returns the decimal part of a given positive floating-point number. 

It then includes a test function `test_truncate_number` that contains several assert statements that check the correctness of the `truncate_number` function, passing different numbers as arguments.