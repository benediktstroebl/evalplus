```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    """
    if number <= 1:  # Handle special case
        return number
    integer = int(number)
    decimal = number - integer
    return decimal
```
The function takes a number and returns the decimal part of the number. It handles the specific cases, if the number is less than or equal to 1, it returns the number directly, and if the number is greater, it returns the decimal part by subtracting the largest integer from the number. The function uses the specific cases to improve the accuracy of the returned decimal part.