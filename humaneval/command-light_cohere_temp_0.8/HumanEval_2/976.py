```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.25 if number <= 1
   
        return number if number <= 0
        else return number // 1
    """

    # Test case 1: Should return 0.25
    test case for numbers <= 1
    return 0.5  #value(3.5)

    # Test case 2: Should return the original number
    return 3.5  #value(3.5)  # Test case 3: Should return 0.0
    test for negative numbers
    return number // 1 for any negative number.