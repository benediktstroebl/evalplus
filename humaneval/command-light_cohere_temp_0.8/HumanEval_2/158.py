```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.1 if number < 1.0 else return int(number -floor(number / 100.0),0.5 + number.5 return float."""
    advantages:
    - Efficient decomposition that avoids overflow, and provides a better guarantee on a wider range of numbers. 
- Rationale for the return value that simplifies the code. 
- Use int() to get the integer part is more readable and standard in Python. 
- The floor() function is used to get the largest integer that is less than or equal to the given number. 
- The / 100.0 operator is used to get the decimal part in a more efficient way and without overflow. 
- The + operator is used to add the integer part and the decimal part together to get the return value.