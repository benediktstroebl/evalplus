### Truncate Number Script

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
        float: The decimal part of the input number.
    
    Example:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)


# Example usage:
if __name__ == "__main__":
    numbers = [3.5, 7.2, 11.1, 15.0]
    for num in numbers:
        print(f"Decimal part of {num}: {truncate_number(num)}")
```

This script defines a function `truncate_number` that calculates the decimal part of a given positive floating point number by subtracting its integer part from the number itself. The example usage demonstrates how to use the function with a list of numbers.