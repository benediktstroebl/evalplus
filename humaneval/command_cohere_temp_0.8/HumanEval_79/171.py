Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_str = bin(decimal)[2:]
    return f"db{binary_str}db"

# Test Cases
decimal = 15
result = decimal_to_binary(decimal)
print(f"Test Case: decimal_to_binary({decimal}) returns {result}")

decimal = 32
result = decimal_to_binary(decimal)
print(f"Test Case: decimal_to_binary({decimal}) returns {result}")
```
This script includes the function `decimal_to_binary`, which takes a decimal number as input and converts it to binary format according to the problem statement. The script also includes test cases to validate the function's behavior. 

The binary string is generated using the `bin` function, which converts the decimal number to a binary string. The first two characters ("db") are added at the beginning and end of the string to maintain the specified format. The final result is a string with characters '0' and '1' representing the binary digits, enclosed by the extra 'db' characters at the beginning and end.

When run, the test cases will print the results, validating the function's behavior, and confirming its ability to convert decimal numbers to the specified binary format.