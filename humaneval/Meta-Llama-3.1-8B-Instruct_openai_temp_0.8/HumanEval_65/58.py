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
        str: The result of the circular shift as a string
    """
    # Convert the integer to a string for easier manipulation
    str_x = str(x)
    
    # Calculate the effective shift, considering cases where shift > len(str_x)
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts at the effective shift position
    first_part = str_x[-effective_shift:]
    second_part = str_x[:-effective_shift]
    
    # Combine the two parts in reverse order to get the circular shift
    result = first_part + second_part
    
    return result

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

This Python script defines the `circular_shift` function that takes an integer `x` and a shift value `shift` as input, performs the circular shift on the digits of `x`, and returns the result as a string. The `circular_shift` function handles cases where the shift value is greater than the number of digits in the input integer by using the modulo operator to calculate the effective shift. The test cases at the end of the script demonstrate the function's behavior with different inputs.