```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    # define constants
    MAX_INT = 10
    DECIMAL_PART = 1e-9  # 1e9th decimal part of the number

    # initialize result
    decimal_part = 0.0

    # calculate decimal part
    decimal_part = number / MAX_INT  # floor division to get rid of fraction part
    # return decimal part
    return decimal_part
```
This solution computes the decimal part of a positive floating point number. The function takes a number, a floating point input and returns its decimal part as a float. The function uses the define constants MAX_INT and DECIMAL_PART to set the maximum integer value and the maximum decimal value that can be stored in a floating point number. The function then calculates the decimal part of the number by dividing the number by MAX_INT and then assigns the result to the variable DECIMAL_PART. The function then returns the decimal part of the number as a float.