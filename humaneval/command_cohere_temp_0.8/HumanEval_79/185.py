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

This script defines a function `decimal_to_binary(decimal)` that takes a decimal number as its input. It uses the `bin` function to convert the decimal number to a binary string, with the format of "dbxxxxxxxxxxdb" where "db" at the beginning and end are added for clarity. The middle part ("xxxxxxxxxx") is extracted using string formatting and the final string is returned.

The test cases are also included, and they assert that the function returns the correct binary strings for the given decimal inputs.