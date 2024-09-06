```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    3.0
"""
```
This function is designed to take a positive floating-point number as input and return the decimal part of the number. The function uses the mathematical operation to split the number into its integer and decimal parts. The logic is that the number is greater than 1, which is the floor function applied to the number and takes the largest integer that is less than or equal to the floor.  The decimal part is the fractional part of the number, which is always less than 1.