```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    -0.299999999999

    """

    Test case #1:
    >>> test_1 = 3.5
    >>> truncate_number(test_1)
    0.29999999999

   

    Test case #2:
    >>> test_2 = 3.2
    >>> truncate_number(test_2)
    0.1

    Test case #3:
    >>> test_3 = 0.5
    >>> truncate_number(test_3)
    0.0
```