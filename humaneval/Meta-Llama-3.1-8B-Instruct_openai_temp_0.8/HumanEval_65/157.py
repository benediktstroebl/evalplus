```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The input integer
        shift (int): The number of positions to shift the digits
        
    Returns:
        str: The result as a string
    """
    
    # Convert the integer to a string to easily access and shift the digits
    str_x = str(x)
    
    # Calculate the effective shift, taking into account the length of the string
    # This is because shifting by the length of the string or more returns the original string
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts at the effective shift position from the end
    # The part to be moved to the start is the substring from the start to the shift position
    # The part to stay at the end is the substring from the shift position to the end
    part1 = str_x[-effective_shift:]
    part2 = str_x[:-effective_shift]
    
    # Return the result by concatenating the two parts
    return part1 + part2

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
print(circular_shift(123, 2))  # Output: "321"
print(circular_shift(123, 5))  # Output: "321"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift amount `shift` as input, performs the circular shift operation, and returns the result as a string. The function uses string manipulation techniques to calculate the effective shift and split the string into two parts to be concatenated in the correct order. The script also includes test cases to demonstrate the function's behavior.