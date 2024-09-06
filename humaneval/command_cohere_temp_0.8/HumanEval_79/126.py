Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_str = bin(decimal)[2:]
    return f"db{binary_str}db"

# Test Cases
decimal = 15
expected_result = "db1111db"
test_result = decimal_to_binary(decimal)
assert test_result == expected_result

decimal = 32
expected_result = "db100000db"
test_result = decimal_to_binary(decimal)
assert test_result == expected_result
```

This script defines the `decimal_to_binary` function, as specified in the problem statement, and provides test cases to validate its correctness. The `bin` function is used to convert the decimal number to a binary string, and then extra bits 'db' are added at the beginning and end to ensure the desired format.