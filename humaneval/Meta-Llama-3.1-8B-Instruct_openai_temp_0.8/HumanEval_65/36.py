```markdown
### Circular Shift of Integer Digits

This Python script defines a function `circular_shift` that takes an integer `x` and the number of positions `shift` to shift its digits.

#### Code

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
        str: The result of the circular shift operation as a string.
    """
    # Convert the integer to a string to easily access and manipulate its digits
    x_str = str(x)
    
    # Calculate the effective shift, which is shift modulo the number of digits
    # This handles the case where shift is greater than the number of digits
    effective_shift = shift % len(x_str)
    
    # Split the string into two parts: the last effective_shift digits and the rest
    # Then concatenate them in reverse order to get the shifted string
    shifted_str = x_str[-effective_shift:] + x_str[:-effective_shift]
    
    return shifted_str

# Example use cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```

#### Explanation

This script works by first converting the input integer to a string. It then calculates the effective shift, which is `shift` modulo the number of digits. This handles cases where `shift` is greater than the number of digits. The script then splits the string into two parts: the last `effective_shift` digits and the rest. It then concatenates these parts in reverse order to get the shifted string.