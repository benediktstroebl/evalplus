```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.

    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer
        shift (int): The number of digits to shift

    Returns:
        str: The shifted integer as a string
    """
    # Convert integer to string for easier manipulation
    str_x = str(x)
    
    # Calculate the effective shift, considering the shift amount and the number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts based on the effective shift
    first_part = str_x[-effective_shift:]
    second_part = str_x[:-effective_shift]
    
    # Return the shifted string by concatenating the two parts
    return first_part + second_part

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift amount `shift` as input, and returns the shifted integer as a string. The function uses the modulo operator (`%`) to calculate the effective shift amount, which is used to split the input string into two parts. The parts are then concatenated in reverse order to form the shifted string. The test cases demonstrate the function's correctness.