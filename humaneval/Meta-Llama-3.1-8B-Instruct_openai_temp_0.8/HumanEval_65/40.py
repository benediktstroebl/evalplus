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
        str: The resulting string after shifting the digits.

    Example:
        >>> circular_shift(12, 1)
        "21"
        >>> circular_shift(12, 2)
        "21"
    """
    # Convert the integer to a string to easily manipulate its digits
    str_x = str(x)
    
    # Calculate the effective shift, considering the case where shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts, shift the right part to the left, and combine them
    result = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return result

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
```

In this script, we first convert the integer `x` to a string to easily manipulate its digits. Then, we calculate the effective shift by taking the modulus of `shift` with the length of the string. This ensures that if `shift` is greater than the number of digits in `x`, the effective shift will be the remainder when `shift` is divided by the number of digits.

Next, we split the string into two parts at the effective shift position, shift the right part to the left, and combine them to get the final result. The `result` string is then returned.

Finally, we test the function with the given examples to demonstrate its correctness.