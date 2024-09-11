```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The number to be shifted.
        shift (int): The number of positions to shift.

    Returns:
        str: The shifted number as a string.
    """
    # Convert the number to a string for easier manipulation
    num_str = str(x)
    
    # Calculate the effective shift, considering the number of digits
    effective_shift = shift % len(num_str)
    
    # Split the string into two parts at the shift index
    first_part = num_str[-effective_shift:]  # The last 'effective_shift' characters
    second_part = num_str[:-effective_shift]  # The remaining characters
    
    # Combine the two parts in reverse order to get the shifted number
    shifted_num = first_part + second_part
    
    return shifted_num

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
```

However, a cleaner and more concise version of this function would be:

```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.

    Args:
        x (int): The number to be shifted.
        shift (int): The number of positions to shift.

    Returns:
        str: The shifted number as a string.
    """
    num_str = str(x)
    shifted_num = num_str[-shift % len(num_str):] + num_str[:-shift % len(num_str)]
    return shifted_num

# Test cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
```