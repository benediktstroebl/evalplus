```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    if number < 0:
        raise ValueError("Input number must be positive.")
    
    # Take advantage of the fact that the modulo operator in Python (%) 
    # can operate on floating point numbers to extract the decimal part.
    return number % 1


# Example use case
if __name__ == "__main__":
    print(truncate_number(3.5))   # Output: 0.5
    print(truncate_number(10.2))  # Output: 0.2
    print(truncate_number(5.0))   # Output: 0.0
```