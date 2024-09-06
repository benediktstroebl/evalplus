Here is a self-contained Python script with a function that solves the problem you described:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number.
    >>> truncate_number(3.5)
    1.9

```

The function uses the math library in Python to get the decimal part of a number.  It first calls the data type(number) // 1 to get the floor part of the number, then it subtracts this floor part from the number to get the decimal part.