```python
def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Subtract the integer part of the number from the number itself
    # The integer part is obtained using the built-in int() function
    # This works because int() truncates the number towards zero
    return number - int(number)

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.25))  # Output: 0.25
print(truncate_number(12.0))  # Output: 0.0
```