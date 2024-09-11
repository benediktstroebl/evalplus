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
    if number < 0:
        raise ValueError("Input number must be a positive floating point number")
    return number - int(number)


# Example usage
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
    print(truncate_number(10.23))  # Output: 0.23
    print(truncate_number(7.9))  # Output: 0.9
```