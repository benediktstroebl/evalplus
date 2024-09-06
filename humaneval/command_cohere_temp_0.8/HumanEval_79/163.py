Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]    
    return 'db' + binary + 'db'

# Test cases
decimal = 15
expected_result = 'db1111db'
result = decimal_to_binary(decimal)

assert result == expected_result
```

In this script, the `decimal_to_binary` function takes a decimal number as its argument and converts it to its binary representation. The `bin` function provides the binary representation of the decimal number, and we extract this representation by slicing the result string from the third character (`[2:]`). We then return the binary representation surrounded by 'db' at the beginning and end to fulfill the problem specification.

The test case `decimal = 15` is provided, and the expected result is calculated using the provided function. The assertion checks that the result of the function corresponds to the expected result.