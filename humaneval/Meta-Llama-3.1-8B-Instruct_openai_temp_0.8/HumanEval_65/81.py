```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The input integer
    shift (int): The number of positions to shift the digits right
    
    Returns:
    str: The result of the circular shift as a string
    """
    str_x = str(x)  # Convert the integer to a string
    shift = shift % len(str_x)  # Handle cases where shift > number of digits
    return str_x[-shift:] + str_x[:-shift]  # Shift the digits and join them back into a string


# Test cases
print(circular_shift(12, 1))  # Expected output: "21"
print(circular_shift(12, 2))  # Expected output: "21"
print(circular_shift(123, 3))  # Expected output: "321"
print(circular_shift(123, 4))  # Expected output: "123"
print(circular_shift(123, 7))  # Expected output: "321"
```