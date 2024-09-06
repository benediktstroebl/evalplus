Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    binary_string = bin(decimal)[2:]
    return f"db{binary_string}db"

# Example usage:
decimal_value = 15
result = decimal_to_binary(decimal_value)
print(result)
```
This script defines a function `decimal_to_binary` that takes a decimal number as input and converts it to its binary representation, according to the problem statement. The function then returns this binary representation surrounded by 'db' characters at the start and end to ensure the result is a string. The example usage demonstrates how to use this function to convert a decimal number to binary.