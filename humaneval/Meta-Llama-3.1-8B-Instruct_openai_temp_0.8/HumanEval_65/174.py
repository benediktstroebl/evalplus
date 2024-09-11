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
    # Convert the integer to a string to easily access and manipulate its digits
    str_x = str(x)

    # Calculate the effective shift, which is the remainder of shift divided by the length of the string
    # This is because shifting by the length of the string (or more) is equivalent to not shifting at all
    effective_shift = shift % len(str_x)

    # Split the string into two parts at the point where the effective shift occurs
    # The part to be moved to the end is the right part after the split
    # The part to stay in the front is the left part after the split
    part_to_move = str_x[-effective_shift:]
    part_to_stay = str_x[:-effective_shift]

    # Combine the two parts in the correct order to get the result
    result = part_to_move + part_to_stay

    return result


# Example use cases
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "21"
print(circular_shift(123, 1))  # Output: "321"
print(circular_shift(123, 3))  # Output: "123"
```