```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number: A positive floating point number.

    Returns:
        The decimal part of the number.
    """
    return number - int(number)


# Example usage
print(truncate_number(3.5))  # Output: 0.5
```

This function works by subtracting the integer part of the number from the original number. The integer part is obtained using the built-in `int()` function, which truncates the decimal part. The result is the decimal part of the number.

Please note that this function does not check if the input number is positive. If you want to add this check, you can modify the function as follows:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number: A positive floating point number.

    Returns:
        The decimal part of the number.

    Raises:
        ValueError: If the input number is not positive.
    """
    if number <= 0:
        raise ValueError("Input number must be positive")
    return number - int(number)


# Example usage
print(truncate_number(3.5))  # Output: 0.5
```