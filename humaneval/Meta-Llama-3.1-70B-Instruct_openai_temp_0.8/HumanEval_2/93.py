```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    >>> truncate_number(3.5)
    0.5
    """
    if number < 0:
        raise ValueError("Input number must be non-negative.")

    integer_part = int(number)
    decimal_part = number - integer_part
    
    return decimal_part

# Test the function
if __name__ == "__main__":
    print(truncate_number(3.5))  # Expected output: 0.5
    print(truncate_number(10.8))  # Expected output: 0.8
    print(truncate_number(5.0))  # Expected output: 0.0
```