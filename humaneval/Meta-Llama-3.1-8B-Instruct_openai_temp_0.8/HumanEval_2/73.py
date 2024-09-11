### Truncate Number Script
```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the input number.

    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


# Example usage
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
    print(truncate_number(4.0))  # Output: 0.0
    print(truncate_number(5))    # Output: 0.0
```
This script defines a function `truncate_number` that takes a positive floating-point number as input, subtracts its integer part, and returns the result. The example usage demonstrates the function's behavior with different inputs.