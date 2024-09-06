Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format
    
    Extra characters 'db' are added at the beginning and end of the string for formatting."""
    binary_str = f"db{bin(decimal)[2:]}.replace('0b', '')"
    return binary_str + "db"

# Test cases
assert decimal_to_binary(15) == "db1111db"
assert decimal_to_binary(32) == "db100000db"
```

This code defines a function `decimal_to_binary` that takes in a decimal number and converts it to binary format. It uses the `bin` function to convert the decimal number to a binary string, then adds the extra characters 'db' at the beginning and end of the string as specified in the problem statement. Finally, it returns the formatted binary string.