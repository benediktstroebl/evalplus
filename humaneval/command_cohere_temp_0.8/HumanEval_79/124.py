Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]     # Convert decimal to binary and remove '0b'
    return f"db{binary}db"       # Add 'db' characters for better formatting

# Test cases
decimal = 15
expected_result = "db1111db"
result = decimal_to_binary(decimal)

if result == expected_result:
    print("Test passed!")
else:
    print("Test failed!")
```

This script defines the `decimal_to_binary` function, which takes a decimal number as its argument and converts it to binary. It uses the `bin` function to convert the decimal to a binary string, and then adds the "db" characters at the beginning and end for better formatting as specified in the problem statement.

The script also includes a test case to check the function's correctness. The test case is defined as a decimal number, and the expected result is hard-coded as a string. The `decimal_to_binary` function is called with the decimal number, and the result is stored in the `result` variable. Finally, the script checks whether the `result` matches the `expected_result`, and it prints either "Test passed!" or "Test failed!" depending on whether the test passed or failed respectively.