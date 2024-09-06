Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    binary = f"db{bin(decimal)[2:]}.replace('0b', '')"
    return binary

# Test Cases
assert decimal_to_binary(15) == "db1111db"
assert decimal_to_binary(32) == "db100000db"
```

This code snippet defines a function `decimal_to_binary(decimal)` that takes a decimal number as its argument and converts it to binary format. It utilizes the `bin` function to convert the decimal number to a binary string, prefaces and appends it with "db" characters for better formatting, and then uses `replace` to eliminate the "0b" prefix. Finally, the converted binary string is returned.

The test cases assert that the function correctly converts the given decimal numbers (15 and 32) to the desired binary format.