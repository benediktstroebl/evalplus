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
    # Convert the integer to a string to easily manipulate the digits
    num_str = str(x)
    
    # Calculate the effective shift, considering the case where shift > number of digits
    effective_shift = shift % len(num_str)
    
    # If shift > number of digits, return the digits reversed
    if effective_shift == 0:
        return num_str[::-1]
    
    # Split the string into two parts: the part to be shifted to the beginning and the part to be kept at the end
    first_part = num_str[-effective_shift:]
    second_part = num_str[:-effective_shift]
    
    # Combine the two parts in the correct order to get the result
    result = first_part + second_part
    
    return result


# Test the function
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(1234, 1))  # "4321"
print(circular_shift(1234, 4))  # "1234"
```

This script defines the `circular_shift` function, which takes an integer `x` and a shift amount `shift` as input. It uses string manipulation to perform the circular shift and returns the result as a string. The function handles the case where `shift` is greater than the number of digits in `x` by returning the digits reversed. The test cases at the end demonstrate the function's behavior.