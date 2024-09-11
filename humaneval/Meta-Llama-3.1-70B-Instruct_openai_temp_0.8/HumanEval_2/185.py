```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    an integer part (largest integer smaller than given number) and decimals 
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    :param number: A positive floating point number.
    :return: The decimal part of the number.
    """
    if not isinstance(number, (int, float)) or number < 0:
        raise ValueError("Input should be a non-negative number")

    # Calculate the integer part of the number
    integer_part = int(number)
    
    # The decimal part is the difference between the number and its integer part
    decimal_part = number - integer_part
    
    return decimal_part


# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.9))  # Expected output: 0.9
print(truncate_number(5))  # Expected output: 0.0
```