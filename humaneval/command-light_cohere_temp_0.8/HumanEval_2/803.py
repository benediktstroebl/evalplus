```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    # integer part calculation
    integer = number // floor(number)

    # decimal part calculation
    remainder = number % floor(number)
    # decimal part = remainder / floor(number)
    return number - (remainder / floor(number))
```
This function takes a positive floating point number as input and returns the decimal part of that number. The decimal part is calculated by dividing the remainder of the number divided by its floor value by the floor value itself. The floor function returns the difference between the whole number and the largest integer less than the input number.