### Truncate Number Script
```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it decomposes it into an integer part 
    (largest integer smaller than given number) and decimals (leftover part always 
    smaller than 1). It returns the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)


# Testing the function
if __name__ == "__main__":
    print(truncate_number(3.5))  # Expected output: 0.5
    print(truncate_number(10.8))  # Expected output: 0.8
    print(truncate_number(5.0))   # Expected output: 0.0
```
This script defines the `truncate_number` function, which calculates the decimal part of a given positive floating point number by subtracting its integer part from the number itself. The function is then tested with different inputs to demonstrate its functionality.