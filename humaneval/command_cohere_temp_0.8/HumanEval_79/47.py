Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]     # Convert decimal to binary and remove '0b'
    return f"db{binary}db"       # Add 'db' characters for better formatting

# Test cases
decimal = 15
expected = "db1111db"
result = decimal_to_binary(decimal)
print(f"Test case: decimal={decimal}, expected={expected}, result={result}")

decimal = 32
expected = "db100000db"
result = decimal_to_binary(decimal)
print(f"Test case: decimal={decimal}, expected={expected}, result={result}")
```

This script defines the `decimal_to_binary` function, which takes a decimal number as its argument and converts it to binary. It uses the `bin` function to convert the decimal to a binary string, strips the '0b' prefix, and then adds 'db' to the beginning and end of the string for better formatting.

The script provides examples and prints the test cases with the expected results for comparison with the output of the `decimal_to_binary` function.