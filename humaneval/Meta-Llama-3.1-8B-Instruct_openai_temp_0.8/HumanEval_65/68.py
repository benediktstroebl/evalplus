```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The number to be shifted.
        shift (int): The number of positions to shift the digits.
    
    Returns:
        str: The shifted number as a string.
    """
    # Convert the integer to a string to easily access and manipulate individual digits
    num_str = str(x)
    
    # Calculate the effective shift (in case shift > number of digits)
    effective_shift = shift % len(num_str)
    
    # Slice the string into two parts, shift the first part to the end, and concatenate them
    shifted_str = num_str[-effective_shift:] + num_str[:-effective_shift]
    
    return shifted_str

# Test the function
if __name__ == "__main__":
    print(circular_shift(12, 1))  # Output: "21"
    print(circular_shift(12, 2))  # Output: "12"
```

In this script, the `circular_shift` function takes an integer `x` and a shift value `shift` as input, performs the circular shift, and returns the result as a string. The `effective_shift` is calculated to handle cases where `shift` is greater than the number of digits in `x`. The function uses Python's string slicing feature to efficiently perform the shift. The script also includes a test section at the end to verify the correctness of the function.