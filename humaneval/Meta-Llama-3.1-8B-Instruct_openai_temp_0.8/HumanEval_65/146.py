```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift.

    Returns:
        str: The shifted digits as a string.
    """
    # Convert the integer to a string to easily access its digits
    str_x = str(x)
    
    # Calculate the effective shift, considering cases where shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts at the effective shift position
    shifted = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return shifted

# Example usage:
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script uses a simple and efficient approach to solve the problem. It converts the input integer to a string, calculates the effective shift (considering cases where shift > number of digits), splits the string into two parts at the effective shift position, and then concatenates them to form the final result. The example usage demonstrates the correctness of the function with the given test cases.