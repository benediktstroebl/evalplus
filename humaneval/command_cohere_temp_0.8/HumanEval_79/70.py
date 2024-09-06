Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    binary_string = bin(decimal)[2:]
    return f"db{binary_string}db"

# Test Cases
assert decimal_to_binary(15) == "db1111db"
assert decimal_to_binary(32) == "db100000db"
```

This script defines a function `decimal_to_binary` that takes a decimal number as input and converts it to its binary representation, with extra "db" characters as specified in the problem statement. The example test cases are included to validate the function's behavior. Make sure to adapt these tests to your specific testing framework for a more comprehensive and organized scenario.