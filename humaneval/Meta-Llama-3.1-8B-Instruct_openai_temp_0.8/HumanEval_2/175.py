```markdown
### Truncate Number Function
#### Truncates the integer part of a given number and returns the decimal part

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    
    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.8))  # Expected output: 0.8
```

This script defines a function `truncate_number` that calculates the decimal part of a given number by subtracting its integer part. It then tests this function with two example inputs to demonstrate its correctness.