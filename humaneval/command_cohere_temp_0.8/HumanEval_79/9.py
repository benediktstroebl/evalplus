Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    db_prefix = "db"
    db_suffix = "db"
    
    # Convert decimal to binary
    binary = bin(decimal)[2:]
    
    # Add db prefixes and suffixes
    binary = db_prefix + binary + db_suffix
    
    return binary

# Test Cases
assert decimal_to_binary(15) == "db1111db"
assert decimal_to_binary(32) == "db100000db"
```

The provided code block contains a problem statement and an example of the expected behavior for the given function. The function `decimal_to_binary` takes a decimal number as its input and returns a string representing the binary equivalent with "db" prefixes and suffixes for better formatting. The test cases confirm that the function behaves as expected for different input values.