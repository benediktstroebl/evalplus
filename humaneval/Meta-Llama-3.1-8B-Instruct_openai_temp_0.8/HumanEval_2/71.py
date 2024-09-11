### Truncate Number Script
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Parameters:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.

    Example:
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


# Example usage:
if __name__ == "__main__":
    # Test the function with known values
    print(truncate_number(3.5))  # Expected output: 0.5
    print(truncate_number(5.0))  # Expected output: 0.0
    print(truncate_number(2.37))  # Expected output: 0.37
```
This Python script defines the `truncate_number` function and includes an example usage section to showcase its functionality. The function works by subtracting the integer part of the number from the original number, effectively leaving only the decimal part. The example usage demonstrates this with three different test cases.