```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The number to be shifted
    shift (int): The number of positions to shift the digits
    
    Returns:
    str: The result of the circular shift as a string
    
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    num_str = str(x)
    num_list = list(num_str)
    
    shift = shift % len(num_str)
    
    # If shift is greater than half the number of digits, we can simplify the problem
    # by shifting the other way (i.e., left), and then reversing the result
    if shift > len(num_str) // 2:
        shift = len(num_str) - shift
    
    # Shift the digits
    num_list = num_list[-shift:] + num_list[:-shift]
    
    return ''.join(num_list)

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift amount `shift` as input, and returns the result of the circular shift as a string. The function works by first converting the integer to a string, and then shifting the characters in the string. If the shift amount is greater than half the number of digits, the function shifts the digits in the other direction (i.e., left) and then reverses the result. The function also uses the modulo operator to simplify the problem by reducing the shift amount to be within the range of the number of digits. Finally, the script tests the function with the examples provided in the problem statement.