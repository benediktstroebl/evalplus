Here's a Python script that solves the problem:
```python
def decimal_to_binary(decimal):
    """Converts a decimal number to its binary representation."""
    binary = '{0:b}'.format(decimal)
    return 'db' + binary + 'db'

# Example usage:
decimal = 15
result = decimal_to_binary(decimal)
print(result)
```

This script defines a function `decimal_to_binary` that takes a decimal number as input and converts it to its binary representation, with extra 'db' characters as specified in the problem statement. 

To run the example, the script converts the decimal number 15 to binary using the `decimal_to_binary` function and then prints the result. The expected output is "db1111db".