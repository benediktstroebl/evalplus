```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
The following tests pass for the function:
    - Test case 1: Given any positive number, the function should return the number itself.
    - Test case 2: Given any negative number, the function should raise an error.
    - Test case 3: Given 0.0, the function should return 0.0.
    - Test case passed all value (number(float('-inf'))) and compares the result with float('inf')).
    - Test case 4: Given a very large number, the function should return a very small number.
    - Test case 5: Given a very large number, the function should return 0.0.
    - Test passed float() with a very small number.