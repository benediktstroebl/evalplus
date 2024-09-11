```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals 
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.
    """
    # Use the modulo operator to get the decimal part
    # This works because (number - int(number))%1 == number%1 
    # due to the properties of rounding down to the nearest integer
    decimal_part = number % 1
    
    return decimal_part

# Test the function
print(truncate_number(3.5))   # Expected output: 0.5
print(truncate_number(4.7))   # Expected output: 0.7
print(truncate_number(5))     # Expected output: 0.0
```

This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. It uses the modulo operator (`%`) to extract the decimal part from the input number. The function is then tested with several examples to demonstrate its correctness.