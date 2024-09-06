```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number
    >>> return 0.5 if number <= 1
   5
    """
    assert number > 1 and number < 5, "Number must be > 1 and < 5"
    assert abs(number - int(number)) <= 1, "Number must be within integer range"
    return int(number) - 1
```
The code defines a function `truncate_number` that takes a float number as input and returns the decimal part of the number. The code uses an assert statement to ensure that the input number is a valid positive floating point number that is greater than 1 and less than 5. The function then uses the `int()` function to get the integer part of the number, and returns the difference between the number and integer part minus 1 to remove the integer part.