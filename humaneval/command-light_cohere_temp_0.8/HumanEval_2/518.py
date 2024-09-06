```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.5 if number <= 1
   LL

    # returns the decimal part
    # testing case 
    return 0.25 / (1LL if number >= 1LL)
``` 
This script defines a function `truncate_number` that returns the decimal part of a given number, as long as the number is greater than `1LL`. The function is designed to handle the case where the number is equal to or less than `1LL` by returning `0.5`, which is` is the integer part of the number, and dividing by `1LL` to ensure the result is a float. The function is also tested for correctness by passing the test `number <= 1LL` and returning `0.5` for any +