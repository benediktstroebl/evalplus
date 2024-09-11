### Truncating Decimal Part of a Number

Here is a Python function that accomplishes the task:

```python
def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Use the built-in floor function from math module which returns the largest integer smaller than or equal to the given number
    from math import floor
    
    # Subtract the integer part from the number
    decimal_part = number - floor(number)
    
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Outputs: 0.5
print(truncate_number(10.7))  # Outputs: 0.7
print(truncate_number(5.0))   # Outputs: 0.0
```

This script uses the built-in `floor` function from the `math` module to get the largest integer smaller than or equal to the given number. The decimal part is then calculated by subtracting this integer part from the original number.