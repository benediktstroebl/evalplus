```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: The decimal part of the number.
    number = abs(number)
    # Calculate the floor integer of the number
    floor_part = int(number)

    # The decimal part is the remainder after dividing by 10
    decimals = number - floor_part
    decimal_part = decimals / 10.

    # Return the above into integers
    decimal_part = decimal_part.
    return decimal_part
```