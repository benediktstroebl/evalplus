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

In this script, the `decimal_to_binary()` function takes a decimal number as its argument and converts it to its binary format. It uses the `bin()` function to convert the decimal number to a binary string, with `bin(decimal)[2:]` trimming off the unnecessary '0b' prefix. The string is then prefixed with "db" and at the end to ensure the desired format with "db" at the beginning and end. Lastly, the `.replace()` method is used to replace "0b" with '' (an empty string) to remove the "0b" prefix from the binary string.