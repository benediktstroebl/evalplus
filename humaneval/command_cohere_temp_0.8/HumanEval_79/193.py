Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary and remove '0b'
    return f"db{binary}db"    # Add 'db' characters for better formatting

# Test cases
assert decimal_to_binary(15) == "db1111db"
assert decimal_to_binary(32) == "db100000db"
```

This script includes a function `decimal_to_binary` that takes a decimal number as input and converts it to binary format. It uses the `bin` function to convert the decimal to a binary string, but it removes the initial '0b' part. Then, it adds the "db" characters at the beginning and end of the string for better output formatting. Finally, the function is tested with the provided example values, ensuring it produces the expected binary strings.