```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.5 if number < 2
    original number
    >>> return 0.5 if number == 1
    good_int(number) <= 2
    >>> return number - 1
    >>> return abs(number) // 1
    >>> return number * 0.5
    return float('inf')
```

The function uses conditional statements to check if the number is a good integer, return 0.5, if the number is less than 2. The function then returns the number - 1, if the number is a good integer. The function also returns the number divided by 1, if the number is a floating point number. 

The function also returns the "inf" keyword, which will raise an exception and the function will return the error as a decimal number.