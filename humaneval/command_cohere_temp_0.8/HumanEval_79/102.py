Here's a Python script with a self-contained function that solves the decimal-to-binary problem and passes the tests:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format"""
    db_prefix = 'db'
    db_suffix = 'db'
    
    # Convert decimal to binary
    binary = bin(decimal)[2:]
    
    # Add db prefixes and suffixes
    binary = db_prefix + binary + db_suffix
    
    return binary

# Test Cases
assert decimal_to_binary(15) == 'db1111db'
assert decimal_to_binary(32) == 'db100000db'
```

The function `decimal_to_binary` takes a decimal number as its argument and returns the binary representation of that number, with '0' and '1' characters. The returned string always begins and ends with extra characters 'db' to indicate the binary format. 

The provided test cases ensure that the function behaves as expected. You can add more tests to cover other decimal numbers and verify that the function's behavior corresponds to the problem statement.