Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    db_prefix = 'db'
    db_suffix = 'db'
    
    binary_str = '{:b}'.format(decimal)
    return f"{db_prefix}{binary_str}{db_suffix}"

# Test cases
decimal = 15
expected_result = 'db1111db'
assert decimal_to_binary(decimal) == expected_result

decimal = 32
expected_result = 'db100000db'
assert decimal_to_binary(decimal) == expected_result
```

In this script, the `decimal_to_binary` function takes a decimal number as its argument and leverages the format specification `{:b}`. This formatting converts the decimal number to a binary string, where `b` denotes binary format. To conform to the specified problem, the function prefaces and suffices the binary string with 'db' characters, ensuring the return output has the desired format. 

The test cases assert that the function's output corresponds to the expected results for the given decimal inputs.