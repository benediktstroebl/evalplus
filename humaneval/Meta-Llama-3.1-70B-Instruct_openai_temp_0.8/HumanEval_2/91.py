```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    :param number: A positive floating point number.
    :return: The decimal part of the number.
    """
    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - int(number)
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.2))  # Output: 0.2
print(truncate_number(5.0))  # Output: 0.0
```