```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift and return the result as a string.
    If shift > len(str(x)), return str(reversed(str(x)))
    # Using built-in str.join reverse method to reverse digits
   
    # Then reverse the reversed digits, then shift the digits right by shift.
    # Finally reverse the the back to the original string.
    return ''.join(str(reversed(str(x)))
# Test cases
assertEqual(circular_shift(12, 1), "21")
assertEqual(circular_shift(12, 2), "12")
assertEqual(circular_shift("hello", 1), "olleh")
assertEqual(circular_shift("hello", 2), "olleh")
```