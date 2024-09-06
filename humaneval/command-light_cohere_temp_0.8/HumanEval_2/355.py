Here's the provided Python script:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number.
    >>> truncate_number(3.5) == 0.25
    1)
    recommended? BEDIA Wrapper.

# The wrapper function 'truncate_number' is a function that takes a floating point number as an argument and returns the decimal part of that number. It does this by calling the integer_part() function, which returns the largest integer that is less than the given number, and dividing the result by 10 to get the decimal part.

The function then returns the result.
```