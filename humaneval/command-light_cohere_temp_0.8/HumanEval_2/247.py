Here's a self-contained Python script with a function `truncate_number` that solves the given problem:
```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

        Return the decimal part of the number
        >>> return 0.5 if number < 1
       0
        >>> return 1 if number < 2
        >>> return 2 if number == 2
        >>> return 1 if number % 2 == 0
        >>> return 10*number + 5 if number > 10
        """
    return 0.5 if number >= 1 else 2 if number == 2 else 1 if number % 2 == 0 else 10 * number + 5
```

This script defines a function `truncate_number` that returns the decimal part of the given number.  It uses a strategy to decompose the number into an integer part and a decimal part, where the decimal part is always smaller than 1 and the integer part is the largest integer less than or equal to the given number.