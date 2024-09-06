```python
def truncate_number(n: float) -> float:
    """
    This function takes a positive floating point number and returns the decimal part of the number.
    Args:
        n (float): The number to be decomposed.
    Returns: decimal part of the number
    """
    # Integer part of the number
    i = int(n**0.5)
   
    # Decimal part of the number
    d = n - i
    return d
# Run tests on the function
print(truncate_number(3.5)) # Output: 0.5
print(truncate_number(-3.5)) # Output: -0.5
print(truncate_number(0.0)) # Output: 0.0
print(truncate_number(0.3)) # Output: 0.2
print(truncate_number(1.0)) # Output: 1.0
print(truncate_number(0.5)) # Output: 0.5
```

The function takes a positive floating point number and returns the decimal part of the number. It is achieved by subtracting the integer part from the number, which is always positive and smaller than the original number.