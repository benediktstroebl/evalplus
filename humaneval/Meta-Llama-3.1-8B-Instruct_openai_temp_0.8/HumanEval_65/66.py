```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.

    If shift > number of digits, return digits reversed.

    Args:
        x (int): The integer to perform circular shift on.
        shift (int): The number of positions to shift the digits.

    Returns:
        str: The result of the circular shift as a string.
    """
    # Convert the integer to a string
    num_str = str(x)
    
    # Calculate the effective shift (considering the case when shift > number of digits)
    effective_shift = shift % len(num_str)
    
    # Perform the circular shift by slicing the string
    shifted_str = num_str[-effective_shift:] + num_str[:-effective_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # Expected output: "21"
print(circular_shift(12, 2))  # Expected output: "12"
```
This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift` as input, performs a circular shift on the digits of `x`, and returns the result as a string. The function uses string slicing to achieve the circular shift. The effective shift is calculated by taking the modulus of the shift value with the length of the string representation of `x`, which handles the case when `shift` is greater than the number of digits in `x`. The test cases are included at the end of the script to demonstrate its correctness.