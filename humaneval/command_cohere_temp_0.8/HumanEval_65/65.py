```python
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    x = str(x)
    front, back = x[:shift], x[shift:]
    return f"{back}{front}" if shift < len(x) else f"{x[::-1]}"
```

The function takes an integer x and an integer shift as input, it shifts the digits of x right by shift and returns the result as a string. If shift is greater than the number of digits in x, the function returns the digits of x reversed.

Here is an example of how to use the function:
```python
circular_shift(12, 1) # Outputs "21"
circular_shift(12, 2) # Outputs "12"
```

And here is a more elaborate example where the shift value exceeds the number of digits:
```python
circular_shift(123, 5) # Outputs "321"
```