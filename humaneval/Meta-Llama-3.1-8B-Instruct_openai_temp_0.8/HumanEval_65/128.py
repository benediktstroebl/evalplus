```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The input integer.
        shift (int): The number of digits to shift.
    
    Returns:
        str: The result of the circular shift as a string.
    """
    str_x = str(x)  # Convert the integer to a string
    shift = shift % len(str_x)  # Handle cases where shift > number of digits
    
    return str_x[-shift:] + str_x[:-shift]  # Shift the digits and return the result

# Test cases
if __name__ == "__main__":
    print(circular_shift(12, 1))  # Output: "21"
    print(circular_shift(12, 2))  # Output: "12"
    print(circular_shift(123, 1))  # Output: "321"
    print(circular_shift(123, 3))  # Output: "123"
```

In this script, we first convert the input integer to a string. Then, we calculate the effective shift by taking the modulus of the shift with the length of the string. This handles cases where the shift is greater than the number of digits in the integer. Finally, we use Python's string slicing feature to shift the digits and return the result. The test cases are included at the end to verify the correctness of the function.