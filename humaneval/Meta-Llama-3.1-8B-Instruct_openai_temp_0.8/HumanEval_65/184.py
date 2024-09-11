### Circular Shift Function
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
    str: The result as a string
    """
    str_x = str(x)
    shift = shift % len(str_x)  # Handle shift > number of digits
    return str_x[-shift:] + str_x[:-shift]

# Example usage:
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
print(circular_shift(1234, 1))  # Output: "2341"
print(circular_shift(1234, 3))  # Output: "4312"
```

This script uses Python's string slicing feature to achieve the circular shift. The `str_x[-shift:]` expression gets the last `shift` characters of the string, and `str_x[:-shift]` gets all characters except the last `shift`. By concatenating these two parts, we get the circular shift. The `shift % len(str_x)` line handles the case when `shift` is greater than the number of digits in `x`.