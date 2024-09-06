```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    >>> return 0.5 if number < 1
   0
    """

    """
    number = number - 1 if number >= 1 else number
    return abs(number) // 1

# Test cases
print(truncate_number(10))       # Output: 5.0
print(truncate_number(0))       # Output: 0.0
print(truncate_number(-10))    # Output: -3.4
print(truncate_number(1))       # Output: 1.0
print(truncate_number(1.1))    # Output: 1.0
print(truncate_number(10.1)) # Output: 2.0
print(truncate_number(1.11)) # Output: 1.1
print(truncate_number(0.9)) # Output: 0.1
print(truncate_number(0.0)) # Output: 0.0
```