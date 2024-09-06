Here's a Python script that solves the problem of converting a decimal number to a binary string, with tests to ensure it's correct:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary string format"""
    bin_str = "{0:b}".format(decimal)
    return "db{0}db".format(bin_str)

# Test cases
decimal = 15
expected_result = "db1111db"
test_result = decimal_to_binary(decimal)

assert test_result == expected_result, f"For {decimal}, expected {expected_result}, but got {test_result}"

decimal = 32
expected_result = "db100000db"
test_result = decimal_to_binary(decimal)

assert test_result == expected_result, f"For {decimal}, expected {expected_result}, but got {test_result}"

print("All tests passed!")
```

This script defines a function `decimal_to_binary()` that takes a decimal number as its argument and converts it to a binary string, with the required extra 'db' characters at the start and end. It then uses `format()` to ensure the binary string is formatted correctly. The code includes test cases to verify its correctness against the provided examples in the problem statement. Finally, it prints "All tests passed!" when both tests pass.