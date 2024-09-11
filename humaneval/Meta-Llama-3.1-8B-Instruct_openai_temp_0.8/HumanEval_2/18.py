```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into an integer part 
    (largest integer smaller than given number) and decimals (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    # Use the floor function from the math module to get the largest integer smaller than the number
    from math import floor
    # Subtract the integer part from the number to get the decimal part
    return number - floor(number)

# Test the function
print(truncate_number(3.5))  # Should print: 0.5
print(truncate_number(10.7))  # Should print: 0.7
```

This script defines a function `truncate_number` that takes a floating point number as input and returns the decimal part of the number. It uses the `math.floor` function to get the largest integer smaller than the number, then subtracts this integer part from the original number to get the decimal part. The script then tests this function with several examples.