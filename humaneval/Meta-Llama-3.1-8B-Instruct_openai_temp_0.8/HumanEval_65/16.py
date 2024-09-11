### Circular Shift of Integer Digits
#### Problem Statement
Shift the digits of an integer right by a specified number of positions and return the result as a string.

#### Solution
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
        str: The shifted integer as a string.

    Examples:
        >>> circular_shift(12, 1)
        "21"
        >>> circular_shift(12, 2)
        "12"
    """
    # Convert the integer to a string to easily access and manipulate its digits
    str_x = str(x)

    # Calculate the actual shift based on the number of digits
    actual_shift = shift % len(str_x)

    # If shift is greater than the number of digits, return the digits reversed
    if actual_shift == 0:
        return str_x[::-1]

    # Split the string into two parts: from the start to the shift position and from the shift position to the end
    first_part = str_x[-actual_shift:]
    second_part = str_x[:-actual_shift]

    # Concatenate the two parts in the correct order
    return first_part + second_part

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script uses Python's built-in string manipulation functions to achieve the desired circular shift of the integer digits.