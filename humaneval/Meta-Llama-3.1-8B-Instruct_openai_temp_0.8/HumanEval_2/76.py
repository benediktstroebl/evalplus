```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    :param number: A positive floating point number.
    :return: The decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Separate the integer and decimal parts using the modulus operator
    integer_part = int(number)
    decimal_part = number - integer_part
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.2))  # Output: 0.2
print(truncate_number(5.0))  # Output: 0.0
```

Note that this function assumes that the input number is a positive floating point number. It uses the modulus operator (`%`) to separate the integer and decimal parts, and then returns the decimal part.