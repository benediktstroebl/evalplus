```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.5 if number <= 1.0
   
    result, otherwise

    if number <= 0:
        return "Invalid input: Please enter a positive number"
    else:
        return number - int(number)
```