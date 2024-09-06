```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    return: decimal part of the number
    """
    # Ensure positive number
    if number < 0:
        number = abs(number)

    # Use python's int() function to convert float to integer
    integer_part = int(number)

    # Return the decimal part
    return float(1e-10) / 10 ** integer_part

# Test the function with some inputs
print(truncate_number(3.5))  # Expected 3.5
print(truncate_number(-3.0))  #-3.0
print(truncate_number('3.8'))  #-3.2
print(truncate_number(0.9))  #0.9
print(truncate_number(0.0))  #0.0
```