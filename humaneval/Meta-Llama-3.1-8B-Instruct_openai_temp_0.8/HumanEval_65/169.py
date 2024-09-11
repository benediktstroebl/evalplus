```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift 
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The input integer
    shift (int): The number of positions to shift the digits
    
    Returns:
    str: The result of the circular shift as a string
    """
    # Convert the integer to a string to easily access and shift the digits
    num_str = str(x)
    
    # Calculate the effective shift, considering the case where shift > number of digits
    effective_shift = shift % len(num_str)
    
    # Split the string into two parts at the effective shift position
    first_part = num_str[-effective_shift:]
    second_part = num_str[:-effective_shift]
    
    # Combine the two parts in reverse order to get the shifted string
    result = first_part + second_part
    
    return result

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines the `circular_shift` function, which takes an integer `x` and a shift amount `shift` as input. It converts the integer to a string, calculates the effective shift, splits the string into two parts at the effective shift position, combines the parts in reverse order, and returns the result as a string. The script also includes two test cases to demonstrate the function's behavior.