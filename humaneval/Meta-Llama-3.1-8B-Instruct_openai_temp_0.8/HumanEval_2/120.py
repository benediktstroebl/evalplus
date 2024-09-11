```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


# Example usage:
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
    print(truncate_number(10.99))  # Output: 0.99
```

This script defines the `truncate_number` function that calculates the decimal part of a given number by subtracting the integer part (obtained by casting the number to an integer using `int(number)`) from the original number. The example usage demonstrates how to use this function with different inputs.