Here is the Python script that implements the `truncate_number` function:
```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Example usage:
print(truncate_number(3.5))   # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
print(truncate_number(2.0))   # Output: 0.0
```
This script defines the `truncate_number` function, which takes a positive floating point number and returns its decimal part by subtracting its integer part. The example usage demonstrates the function's behavior with different inputs.