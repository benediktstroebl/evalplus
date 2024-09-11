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


# Example use case:
if __name__ == "__main__":
    print(truncate_number(3.5))  # Outputs: 0.5
    print(truncate_number(10.25))  # Outputs: 0.25
    print(truncate_number(7.99))  # Outputs: 0.99
```