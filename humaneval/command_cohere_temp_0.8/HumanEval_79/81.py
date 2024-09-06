Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary and remove '0b'
    return f"db{binary}db"     # Add 'db' characters for better formatting

# Test cases
decimal = 15
expected_result = "db1111db"
test_result = decimal_to_binary(decimal)

assert test_result == expected_result, f"For decimal {decimal}, expected binary {expected_result} but got {test_result}"

decimal = 32
expected_result = "db100000db"
test_result = decimal_to_binary(decimal)

assert test_result == expected_result, f"For decimal {decimal}, expected binary {expected_result} but got {test_result}"
```

This script defines the `decimal_to_binary` function, which takes a decimal number as its argument and converts it to binary. It uses the `bin` function to convert the decimal to a binary string, excluding the initial '0b'. Then, it adds the 'db' characters at the beginning and end of the binary string for better output formatting. The provided test cases assert that the function produces the expected results for two different decimal numbers.