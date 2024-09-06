```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number.
    """
    example:
    >>> truncate_number(3.5)
    0.1

   
    straightforward way to the number to the original number with decimals less than 1.

    Test cases:
    >>> test_case = (1, 0.0, 0)
    >>> test_case
    (2.5, 0.1, 0)
    Test case 1:
    >>> test_case
    TruncateNumber((1.0, 0, 0))
    0.1

    Test case 2:
    >>> test_case
    TruncateNumber((5.2, 0, 0))
    0.5

    Test case 3:
    >>> test_case
    TruncateNumber((3.5, 0, 0))
    0.1
    """