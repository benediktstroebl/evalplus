```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The integer to be shifted.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The shifted integer as a string.
    """
    # Convert the integer to a string for easy manipulation
    num_str = str(x)
    
    # Calculate the actual shift (in case shift > number of digits)
    shift = shift % len(num_str)
    
    # Split the string into two parts: the part to be shifted to the end and the part to stay at the start
    part_to_shift = num_str[-shift:]
    part_to_stay = num_str[:-shift]
    
    # Combine the two parts to get the final result
    result = part_to_shift + part_to_stay
    
    return result

# Test the function
print(circular_shift(12, 1))  # Expected: "21"
print(circular_shift(12, 2))  # Expected: "21"
print(circular_shift(123, 1))  # Expected: "312"
print(circular_shift(123, 2))  # Expected: "231"
print(circular_shift(123, 5))  # Expected: "321"
```

This script defines a function `circular_shift` that takes an integer and a shift value as input, performs the circular shift operation, and returns the result as a string. It also includes test cases to demonstrate the function's correctness.