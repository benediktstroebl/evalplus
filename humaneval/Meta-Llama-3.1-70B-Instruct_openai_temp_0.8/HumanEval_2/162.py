```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
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
    print(truncate_number(10.2))  # Output: 0.2
    print(truncate_number(7.9))  # Output: 0.9
```

This script defines the `truncate_number` function as specified, and then tests it with a few examples in the `if __name__ == "__main__":` block. The `truncate_number` function works by subtracting the integer part of the number (obtained with `int(number)`) from the original number. This leaves the decimal part, which is then returned.