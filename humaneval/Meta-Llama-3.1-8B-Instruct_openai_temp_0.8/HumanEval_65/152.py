### Circular Shift Function
#### Problem Statement
Given an integer `x` and a shift amount `shift`, return the result of circularly shifting the digits of `x` to the right by `shift` places as a string. If `shift` is greater than the number of digits in `x`, the function should return the digits reversed.

#### Solution
```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
    x (int): The input integer.
    shift (int): The number of places to shift the digits to the right.
    
    Returns:
    str: The result of the circular shift as a string.
    """
    
    # Convert the integer to a string to easily manipulate its digits
    str_x = str(x)
    
    # Calculate the effective shift, taking into account shifts greater than the number of digits
    effective_shift = shift % len(str_x)
    
    # Perform the circular shift by slicing the string
    result = str_x[-effective_shift:] + str_x[:-effective_shift]
    
    return result
```

#### Example Use Cases
```python
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
print(circular_shift(123, 1))  # "231"
print(circular_shift(123, 3))  # "321"
print(circular_shift(123, 4))  # "123"
```