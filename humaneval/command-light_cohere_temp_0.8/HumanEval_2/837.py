```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.5 if number < 0.5
   
    particular
    especially for markdown, where line breaks are represented by spaces.
    """
    number = float(input())
    i = math.ceil(number)
    decimal = 0
    while i >= 1 and i.5 <= number:
        decimal += 1
        i -= 1
    return decimal
```