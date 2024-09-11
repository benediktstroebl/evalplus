```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily access and manipulate its digits
    str_x = str(x)

    # Calculate the actual shift, in case it's greater than the number of digits
    actual_shift = shift % len(str_x)

    # Split the string into two parts at the actual shift point
    part1 = str_x[-actual_shift:]
    part2 = str_x[:-actual_shift]

    # Combine the two parts in reverse order to get the shifted string
    result = part1 + part2

    return result

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift `shift` as input, and returns the result of the circular shift as a string. It uses string manipulation to achieve this, and includes tests to verify its correctness.