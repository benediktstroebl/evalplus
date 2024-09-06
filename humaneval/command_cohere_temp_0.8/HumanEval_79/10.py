Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    db_prefix = 'db'
    db_suffix = 'db'
    
    # Convert decimal to binary
    binary = bin(decimal)[2:]
    
    # Ensure leading zeros
    padded_binary = '0' * (len(db_prefix) - len(binary)) + binary + '0' * (len(db_suffix) - len(binary))
    
    return db_prefix + padded_binary + db_suffix

# Test cases
decimal = 15
expected_result = 'db1111db'
result = decimal_to_binary(decimal)

if result == expected_result:
    print("Test passed!")
else:
    print("Test failed!")
```
This script defines the `decimal_to_binary` function, which takes a decimal number as its argument and returns the binary representation with the leading 'db' characters. The script then tests the function with a test case and prints whether the test passed or failed. You can use this code to verify your solution against the provided tests. Feel free to adapt it to new test cases if needed.