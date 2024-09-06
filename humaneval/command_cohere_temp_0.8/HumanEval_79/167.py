Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_string = "{0:b}".format(decimal)
    return "db{0}db".format(binary_string)

# Example usage:
decimal = 15
result = decimal_to_binary(decimal)
print(result)  # Outputs: db1111db

decimal = 32
result = decimal_to_binary(decimal)
print(result)  # Outputs: db100000db
```

This script defines a function `decimal_to_binary` that takes a decimal number as input and converts it to its binary representation, with extra "db" characters as specified in the problem statement. The format specification `{0:b}`. is used to convert the decimal number to a binary string, and `db{0}db`. is used to add the extra characters 'db' at the beginning and end of the string.