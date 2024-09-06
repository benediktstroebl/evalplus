Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    binary_string = '{0:b}'.format(decimal)
    return 'db' + binary_string + 'db'

# Example usage:
decimal = int(input("Enter a decimal number: "))
result = decimal_to_binary(decimal)
print(result)
```

In this script, the `decimal_to_binary` function takes a decimal integer as input and uses the `{0:b}`.format()` format specifier to convert the decimal number to a binary string. The 'db' characters are prepended and appended to maintain the specified format with extra characters 'db' at the beginning and at the end of the string. The result is then returned as a string.