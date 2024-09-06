```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.1 - (number < 1)
    """
# Test cases:
print(truncate_number(3.5))  # output: 0.2
print(truncate_number(-3.5)) # output: -0.7999999999999999997

print(truncate_number(0.01))  # output: 0.01
print(truncate_number(0.999)) # Input must be a float value, otherwise the function will raise an error.