Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided Markdown code block:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary and remove '0b' prefix
    return f"db{binary}db"    # Add 'db' characters for better formatting

# Test cases
assert decimal_to_binary(15) == "db1111db"
assert decimal_to_binary(32) == "db100000db"
```

This script includes a function `decimal_to_binary` that takes a decimal number as input and converts it to binary format. It uses the built-in `bin` function to convert the decimal to binary, and then removes the '0b' prefix added by `bin`. Finally, it adds 'db' characters at the beginning and end of the binary string for better output formatting.

The test cases are also provided to verify the function's behavior against the expected outputs. Adjust these tests or add more of them to ensure the function's correctness for different input scenarios.