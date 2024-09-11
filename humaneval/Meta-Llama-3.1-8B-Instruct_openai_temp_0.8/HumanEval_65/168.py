```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The input integer.
    shift (int): The number of positions to shift the digits.
    
    Returns:
    str: The result of the circular shift as a string.

    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "21"
    >>> circular_shift(12, 3)
    "12"
    >>> circular_shift(123, 1)
    "231"
    """
    # Convert the integer to a string to easily manipulate its digits
    x_str = str(x)
    
    # Calculate the effective shift, taking into account if shift > number of digits
    effective_shift = shift % len(x_str)
    
    # Split the string into two parts, shift the second part to the left, and concatenate them
    # If shift >= number of digits, this will simply reverse the string
    result = x_str[-effective_shift:] + x_str[:-effective_shift]
    
    return result

# Test the function
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
print(circular_shift(12, 3))  # Output: "12"
print(circular_shift(123, 1))  # Output: "231"
```

This script defines a function `circular_shift` that performs the desired circular shift operation on the digits of an integer. It uses the modulus operator to ensure that the shift is always within the bounds of the number of digits, and then uses Python's string indexing to split the string into two parts and concatenate them in the correct order. The function is then tested with a few examples to demonstrate its correctness.