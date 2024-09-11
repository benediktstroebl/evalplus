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
    # We can get the integer part of the number by using the int() function
    # This will truncate the number, effectively rounding down to the nearest whole number
    integer_part = int(number)
    
    # Now, we subtract the integer part from the original number
    # This will give us the decimal part
    decimal_part = number - integer_part
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
```

Alternatively, you can also use the `math.modf()` function to achieve the same result in a more concise way:

```python
import math

def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    # math.modf() returns a tuple containing the fractional and integer parts of the number
    # We are only interested in the fractional part, so we return the first element of the tuple
    return math.modf(number)[0]

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
```