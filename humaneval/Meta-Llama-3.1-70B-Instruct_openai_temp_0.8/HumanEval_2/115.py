```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.
    """
    # Calculate the integer part of the number using int() function
    # This will truncate the decimal part
    integer_part = int(number)
    
    # Subtract the integer part from the original number to get the decimal part
    decimal_part = number - integer_part
    
    return decimal_part


# Test the function
if __name__ == "__main__":
    print(truncate_number(3.5))  # Expected output: 0.5
    print(truncate_number(10.23))  # Expected output: 0.23
    print(truncate_number(5.9))   # Expected output: 0.9
```

Alternatively, you could also use the `math.modf()` function which can be more efficient and Pythonic:

```python
import math

def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.
    """
    return math.modf(number)[0]


# Test the function
if __name__ == "__main__":
    print(truncate_number(3.5))  # Expected output: 0.5
    print(truncate_number(10.23))  # Expected output: 0.23
    print(truncate_number(5.9))   # Expected output: 0.9
```