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

In this script, the `decimal_to_binary()` function takes a decimal number as input and leverages Python's `bin()` function to convert the decimal number to a binary string. The expression `bin(decimal)[2:]` extracts the binary representation of the number, excluding the redundant '0b' prefix. Subsequently, the `.replace()` method removes the '0b' prefix from the binary string. To ensure a balanced format, two extra characters 'db' are added at the beginning and end of the string.