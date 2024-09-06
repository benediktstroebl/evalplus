Here is a Python script that demonstrates the solution to the problem with markdown code:
```python
def truncate_number(number):
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    """
    special cases for non-integer inputs."""
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a positive floating point number")
    number %= 1e9 + 7
    return number // 1e9 + 7
```
This script defines a function `truncate_number` that takes a number as input and returns the decimal part of the number. The function first checks whether input is either not a positive floating point number. Then it uses the result and the formula for the decimal part of a number to the given input. The result is rounding the decimal part up to the nearest integer and adding 7 to it to get the integer part of the number.