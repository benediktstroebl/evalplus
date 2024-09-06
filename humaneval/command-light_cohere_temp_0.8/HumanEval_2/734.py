```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    """
    # DECOMPOSITION
    number = abs(number) # to avoid negative number
    if number < 2:  # less than 2, means only 1s are present, so only 1 left and number itself 
        return number
    elif number < 5: 
        return round(number) + (number - 5)
    elif number < 10:
        return round(number) + (number - 10)
    else:
        return round(number)
```
The provided Python script defines a function `truncate_number` that takes a number as input and generates the decimal part of the number. The function uses a analytical approach to decompose the number into its integer part and decimal part. The function has different cases based on the input number and applies the appropriate operations to obtain the desired result.