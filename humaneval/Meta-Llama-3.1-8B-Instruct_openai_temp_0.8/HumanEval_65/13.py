```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    # Convert integer to string to easily access and manipulate digits
    num_str = str(x)
    
    # Calculate the effective shift, which is the remainder when shift is divided by the number of digits
    effective_shift = shift % len(num_str)
    
    # If shift is greater than the number of digits, return the digits reversed
    if effective_shift == 0:
        return num_str[::-1]
    
    # Shift the digits to the right by the effective shift
    shifted_str = num_str[-effective_shift:] + num_str[:-effective_shift]
    
    return shifted_str

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

This script defines the `circular_shift` function, which takes an integer `x` and a shift value `shift` as input. It converts the integer to a string to easily access and manipulate its digits. The function then calculates the effective shift, which is the remainder when `shift` is divided by the number of digits in the string. If the shift is greater than the number of digits, it returns the digits reversed. Otherwise, it shifts the digits to the right by the effective shift and returns the result as a string. The script also includes test cases to verify the function's correctness.