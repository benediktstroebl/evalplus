Here is a Python script with a self-contained function that solves the problem you have described:

```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.5 if number < 0
   1
    """

    if number < 0:
        return "Error: Input number should be positive"

    # Perform floating point arithmetic on number and 1
    number_with_1 = number * 1
    decimals = number_with_1 - 1  # Remove the integer part
    return decimals
```
This script defines a function called `truncate_number` that takes a number as input and returns the decimal part of the number. 

The function performs a floating point arithmetic operation on the number and 1 to remove the integer part and returns the difference between the result and 1, which is equivalent to the decimal part of the number.