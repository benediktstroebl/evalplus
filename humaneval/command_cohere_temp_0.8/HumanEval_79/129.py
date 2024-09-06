Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]    
    return 'db' + binary + 'db'

# Test Cases
decimal = 15
expected_result = 'db1111db'
print(f'Test Case: decimal_to_binary({decimal}) == {expected_result}')
assert decimal_to_binary(decimal) == expected_result

decimal = 32
expected_result = 'db100000db'
print(f'Test Case: decimal_to_binary({decimal}) == {expected_result}')
assert decimal_to_binary(decimal) == expected_result
```

This script defines the `decimal_to_binary` function, as specified in the problem statement, and includes test cases to validate the function's behavior against expected outputs. Adjust the test case values as needed.