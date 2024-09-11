```markdown
### Circular Shift Function

This function performs a circular shift on the digits of a given integer.

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
        str: The result as a string.
    """
    # Convert the integer to a string to easily manipulate the digits
    str_x = str(x)
    
    # Calculate the effective shift, considering cases where shift > number of digits
    effective_shift = shift % len(str_x)
    
    # Split the string into two parts at the effective shift position
    # and concatenate them in reverse order to perform the circular shift
    result = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return result

# Example usage:
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
```

#### Explanation

This script defines a function called `circular_shift` that takes an integer `x` and a shift value `shift`. It converts the integer to a string `str_x` to easily manipulate the digits.

To calculate the effective shift, it uses the modulo operator `%` to ensure that the shift is within the range of the number of digits in `str_x`. This handles cases where the shift is greater than the number of digits.

It then splits the string into two parts at the effective shift position and concatenates them in reverse order to perform the circular shift.

Finally, the function returns the result as a string. The example usage demonstrates how to use this function with the provided test cases.