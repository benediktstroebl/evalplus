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
    # Convert the integer to a string to easily access and manipulate the digits
    num_str = str(x)

    # Calculate the effective shift, which is the remainder of shift divided by the number of digits
    # This is because shifting by the number of digits is equivalent to not shifting at all
    effective_shift = shift % len(num_str)

    # If the effective shift is 0, return the original string (i.e., no shift)
    if effective_shift == 0:
        return num_str

    # Split the string into two parts: the part to be shifted to the end and the part to remain at the beginning
    first_part = num_str[-effective_shift:]
    second_part = num_str[:-effective_shift]

    # Combine the two parts in the reverse order to get the shifted string
    result = first_part + second_part

    return result

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift`, and returns the result of shifting the digits of `x` to the right by `shift` positions. The function uses the modulo operator (`%`) to calculate the effective shift, which is the remainder of `shift` divided by the number of digits in `x`. If the effective shift is 0, the function returns the original string. Otherwise, it splits the string into two parts, shifts the first part to the end, and combines the two parts to get the final result. The script includes test cases to demonstrate the function's behavior.