```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    """
    if number < 0:
        return 0.0
    elif number < 10:
        return number - 1
    else:
        return number - 1.1
```
The above Python script defines a function called `truncate_number` that takes a single argument `number` which is a float. It returns the value of the integer part of the number. This is script is designed to work with positive numbers only.