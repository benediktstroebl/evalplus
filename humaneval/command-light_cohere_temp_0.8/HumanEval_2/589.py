```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number.
    """
    integer part = floor(number / 10)
    """
    return 10 * (number / 10)
```
This function takes a number as input and returns the decimal part of the number, rounded up to the nearest integer. 

The function first computes the integer part of the number by using the `floor` function to get the largest integer that is smaller than the given number. 

The function then returns 10 * (number / 10), which will give the decimal part of the number, rounded up to the nearest integer.