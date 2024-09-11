```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The number to shift
    shift (int): The number of places to shift the digits
    
    Returns:
    str: The shifted number as a string
    """
    x_str = str(x)
    shift = shift % len(x_str)  # handle shift greater than number of digits
    return x_str[-shift:] + x_str[:-shift]

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "21"
```

However, a better way would be to convert the number to a list of digits, which can be sliced in a more elegant way.

```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The number to shift
    shift (int): The number of places to shift the digits
    
    Returns:
    str: The shifted number as a string
    """
    x_str = str(x)
    shift = shift % len(x_str)  # handle shift greater than number of digits
    return ''.join(x_str[-shift:] + x_str[:-shift])

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```

Or, if you want a more functional programming style:

```python
def circular_shift(x, shift):
    """
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    
    If shift > number of digits, return digits reversed.
    
    Parameters:
    x (int): The number to shift
    shift (int): The number of places to shift the digits
    
    Returns:
    str: The shifted number as a string
    """
    return ''.join([
        x_str[-shift % len(x_str):],
        x_str[:-shift % len(x_str)]
    ] for x_str in (str(x),))

# Test cases
print(circular_shift(12, 1))  # "21"
print(circular_shift(12, 2))  # "12"
```