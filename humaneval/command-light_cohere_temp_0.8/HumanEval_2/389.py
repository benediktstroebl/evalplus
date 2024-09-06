```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    integer = 0
    while number > 0:
        number -= number // 10
    integer += 1
    return float(number - integer * 10)
```
This Python function, `truncate_number`, takes a number as input and quickly computes and returns the decimal part of the number. It does this technique of repeatedly subtracting the 10's largest integer that would fit within the number while iterating through the number's digits until the number becomes 0. The integer component that resulting from these operation represents the most significant digit, and the fractional component is the remaining digits. This function is efficient approach to achieve this result and offers a clear illustration of how to break down and extract the decimal component of a floating-point number.