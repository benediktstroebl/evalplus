Here's the self-contained Python function that solves the problem you described: 

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    """
    number = float(number)
    if number < 2:
        return 0.0
    elif number < 10:
        return number - 1
    else:
        return number - 2.5  #
``` 

This function takes a positive floating point number as an argument and returns the decimal part of the number. It does this following: 
    - If the input is less than 2, the function returns 0.0.
    - If ver the goal.
    - If goal. If the input is less than than 10, the function returns the original number without decimal part.
    - If goal.If the input is larger than 10, the function returns the original number without decimal part.