Here's a Python script that solves the problem:
```python
def decimal_to_binary(decimal):
    """Converts a decimal number to its binary representation with 0s and 1s surrounded by 'db'"""
    bin_str = '{0:b}'.format(decimal)
    return f'db{bin_str}db'
```

This script provides a function `decimal_to_binary` that takes a decimal number as input and returns its binary representation. The built-in `format` method is used to convert the decimal number to a binary string (`0` or `1`) and then wrapped with `db` at the beginning and end for the specified format. 

The `db` characters are added to the beginning and end of the string to ensure that the output has a consistent format. This is a common technique used in programming challenges to confirm that a user-submitted solution is correctly implementing the logic for converting to binary, as it's trivial to verify that the input decimal numbers map to the expected binary numbers bounded by `db`. 

The function is designed to be self-contained, meaning that it does not rely on any external variables or functions other than those defined in the challenge statement. 

This solution is relatively efficient since it utilizes a built-in Python method (`format`). The solution is adaptable to different decimal numbers and efficiently produces the corresponding binary representation with the specified format. 
```python
decimal = 15
result = decimal_to_binary(decimal)
print(result)  # Should print: db1111db

decimal = 32
result = decimal_to_binary(decimal)
print(result)  # Should print: db100000db
```