```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string to easily access and manipulate individual digits
    num_str = str(x)
    
    # Calculate the effective shift, taking into account if the shift is greater than the number of digits
    effective_shift = shift % len(num_str)
    
    # Split the string into two parts at the shift position
    first_part = num_str[-effective_shift:]
    second_part = num_str[:-effective_shift]
    
    # Combine the two parts in reverse order to achieve the circular shift
    result = first_part + second_part
    
    return result

# Test the function
print(circular_shift(12, 1))  # Expected output: "21"
print(circular_shift(12, 2))  # Expected output: "12"
```

This Python script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input and returns the result of the circular shift as a string. The function first converts the integer to a string to easily access and manipulate individual digits. It then calculates the effective shift by taking the modulus of the shift with the number of digits in the string. The function splits the string into two parts at the shift position, combines them in reverse order, and returns the result. The script includes test cases to demonstrate the function's correctness.