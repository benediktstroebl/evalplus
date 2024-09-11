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
    
    # Use the built-in modulo operator to get the decimal part
    return number % 1


# Test the function
if __name__ == "__main__":
    print(truncate_number(3.5))  # Expected output: 0.5
    print(truncate_number(10.2))  # Expected output: 0.2
    print(truncate_number(5))  # Expected output: 0.0
```