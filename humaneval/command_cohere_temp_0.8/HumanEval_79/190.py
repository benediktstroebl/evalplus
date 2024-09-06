Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    binary = f"db{bin(decimal)[2:]}.replace('0b', 'db')[:-3]"
    return binary

# Test Cases
decimal = 15
result = decimal_to_binary(decimal)
print(f"Test Case: decimal_to_binary({decimal}) = {result}")

decimal = 32
result = decimal_to_binary(decimal)
print(f"Test Case: decimal_to_binary({decimal}) = {result}")
```

In the code above, the `decimal_to_binary` function accepts a decimal number as its argument and converts it to binary format. It uses the `bin` function to convert the decimal number to a binary string, then adds 'db' prefixes at the beginning and ends to maintain the desired format. The `replace` and `[:-3]` slices are used to clean up the '0b' and 'db' remnants. The test cases are also provided to demonstrate the function's behavior.