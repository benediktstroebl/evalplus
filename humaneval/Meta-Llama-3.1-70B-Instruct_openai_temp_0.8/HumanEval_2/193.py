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
        raise ValueError("Input number should be a positive floating point number.")
    
    # Use the modulo operator to get the decimal part
    decimal_part = number % 1
    
    return decimal_part


# Example usage
if __name__ == "__main__":
    number = 3.5
    result = truncate_number(number)
    print(f"The decimal part of {number} is: {result}")
```