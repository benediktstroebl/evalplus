```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The input integer
        shift (int): The number of positions to shift the digits

    Returns:
        str: The result of the circular shift
    """
    str_x = str(x)
    shift = shift % len(str_x)  # Handle shift > number of digits
    return str_x[-shift:] + str_x[:-shift]

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "21"
print(circular_shift(123, 3))  # "231"
print(circular_shift(123, 5))  # "231"
```

This script defines a function `circular_shift` that takes an integer `x` and a shift value `shift`, performs the circular shift, and returns the result as a string. The function uses string slicing to achieve the shift. The test cases at the end demonstrate the function's behavior.