```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
def test_and_assert(number, expected):
    return truncate_number(number) == expected
```
The function `truncate_number` takes a floating point number as input and returns the decimal part of that number. The function uses the decomposition technique, where the decimal part of a positive number is always less than the integer part. The function then returns the value of the number.

The function `test_and_assert` is a helper function that takes two arguments and returns `True` if the first argument is equal to the second argument. This is function is used to test the `truncate_number` function with various inputs.