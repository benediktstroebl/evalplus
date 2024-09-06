```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.
    >>> truncate_number(3.5) == 0.5
def test_decimals(number: float) -> bool:
    """
    Return True if the number has decimals.
    >>> test_decimals(3.5) == False
   
   ```
The function has two inputs, a number, and an optional parameter test, which is a boolean that specifies whether the number should be tested against the condition. The function returns the fact or if the number has decimals, and the parameter test is False. The function returns False if the number has decimals, and the parameter test is True.