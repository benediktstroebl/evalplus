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

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    # Use the built-in modulo operator to get the decimal part of the number
    return number - int(number)


# Test the function
if __name__ == "__main__":
    assert truncate_number(3.5) == 0.5
    assert truncate_number(10.8) == 0.8
    assert truncate_number(0.9) == 0.9
    print("All tests passed.")
```

This script defines the `truncate_number` function as requested. The function works by subtracting the integer part of the number from the original number, effectively leaving only the decimal part.

The script also includes test cases to verify the correctness of the function. If the function is correct, the script will print "All tests passed."