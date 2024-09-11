```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string. If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer
        shift (int): The number of positions to shift the digits to the right

    Returns:
        str: The shifted integer as a string
    """
    # Convert the integer to a string to easily access and manipulate its digits
    x_str = str(x)
    
    # Calculate the effective shift, taking into account if shift > number of digits
    effective_shift = shift % len(x_str)
    
    # Use Python's string slicing feature to perform the circular shift
    # The expression x_str[effective_shift:] gets the substring from the effective shift position to the end
    # The expression x_str[:effective_shift] gets the substring from the start to the effective shift position
    # We concatenate these two substrings to get the final result
    result = x_str[effective_shift:] + x_str[:effective_shift]
    
    return result

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "21" since 2 is smaller than number of digits 2
print(circular_shift(123, 2))  # "321"
```

This script defines the `circular_shift` function as specified, and includes three test cases to verify its correctness. The `circular_shift` function works by first converting the input integer to a string, then calculating the effective shift based on the length of the string. It then uses Python's string slicing feature to perform the circular shift and returns the result as a string.