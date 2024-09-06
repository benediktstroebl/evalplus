```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Returns the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
   
    time can hours that be considered within the function, and test-suite could be imported and used to test it using the assert statement, which would pass the test if the function's output is equal to the expected value.