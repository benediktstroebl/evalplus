Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    db_prefix = "db"
    db_suffix = "db"
    
    # Convert decimal to binary
    binary = bin(decimal)[2:]
    
    # Ensure leading zeros
    padded_binary = ("0" * (len(db_prefix) - len(binary)) + binary) + ("0" * (len(db_suffix) - len(binary)))
    
    # Return the formatted binary string
    return db_prefix + padded_binary + db_suffix

# Test cases
decimal = 15
expected_result = "db1111db"
actual_result = decimal_to_binary(decimal)

assert actual_result == expected_result, f"For decimal {decimal}, expected binary {expected_result}, but got {actual_result}"

decimal = 32
expected_result = "db100000db"
actual_result = decimal_to_binary(decimal)

assert actual_result == expected_result, f"For decimal {decimal}, expected binary {expected_result}, but got {actual_result}"

decimal = -1
expected_result = "db11111111db"
actual_result = decimal_to_binary(decimal)

assert actual_result == expected_result, f"For decimal {decimal}, expected binary {expected_result}, but got {actual_result}"
```

This script defines the `decimal_to_binary` function as described in the problem statement. It converts the decimal number to binary, pads the binary string with leading zeros to match the desired format, and adds the "db" prefixes and suffixes as requested. Then, three test cases are provided to validate the function's behavior for different input values.