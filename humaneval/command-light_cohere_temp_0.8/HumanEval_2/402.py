```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
   > 0.25
```
The code provides a function that takes a number and returns the decimal part of that number. It uses Python's max function to get the largest integer less than the given number and subtracts it from the number to get the leftover part. This is result is then always smaller than 1, so the function returns the leftover part as a float.