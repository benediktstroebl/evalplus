Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    db_prefix = 'db'
    db_suffix = 'db'
    
    binary_string = bin(decimal)[2:]
    binary_string = binary_string.zfill(len(bin(decimal)[2:]) + 2*len(db_prefix) + len(db_suffix))
    
    return db_prefix + binary_string + db_suffix

# Test cases
decimal = 15
expected_result = 'db1111db'
result = decimal_to_binary(decimal)

assert result == expected_result, f"For {decimal}, expected {expected_result}, but got {result}"

decimal = 32
expected_result = 'db100000db'
result = decimal_to_binary(decimal)

assert result == expected_result, f"For {decimal}, expected {expected_result}, but got {result}"

decimal = -1
expected_result = 'db11111111db'
result = decimal_to_binary(decimal)

assert result == expected_result, f"For {decimal}, expected {expected_result}, but got {result}"

decimal = 0
expected_result = 'db00000000db'
result = decimal_to_binary(decimal)

assert result == expected_result, f"For {decimal}, expected {expected_result}, but got {result}"

decimal = 123
expected_result = 'db11112211db'
result = decimal_to_binary(decimal)

assert result == expected_result, f"For {decimal}, expected {expected_result}, but got {result}"
```

This script defines the `decimal_to_binary` function, which takes a decimal number as its argument and converts it to binary format, with 'db' prefixes and suffixes added for clarity. Then, the function is tested with different test cases, checking whether the returned value corresponds to the expected binary format.

Note that this solution doesn't require any external dependencies like `numpy` or `binascii`, as it uses the built-in `bin` function for conversion, and `zfill` for right padding with '0's.