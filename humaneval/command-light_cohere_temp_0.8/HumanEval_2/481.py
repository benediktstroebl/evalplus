```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

        Return the decimal part of the number.
    number = float(number)
    if number < 0:
        return "NO"
    if number < 10:
        return number
    # The following condition is to handle special cases where the number
    # is a perfect power of 2.
    # which is decimal part will be always 0
    i = len(str(number)) - 2
    while i >= 0:
        if int(str(number)[i]) != 0:
            break
        number = float(str(number)[-i])
        i -= 1
    return number
``` 
This code provides a function that takes a floating point number as input and returns the decimal part of the number.