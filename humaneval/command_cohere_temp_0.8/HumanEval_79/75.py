Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    binary_str = '{0:b}'.format(decimal)
    return 'db' + binary_str + 'db'

# Example usage:
decimal_value = 15
result = decimal_to_binary(decimal_value)
print(result)  # Output: db1111db
```

In this script, the built-in `format` method is used with a formatting specifier `{0:b}`. This specifier instructs the method to format the integer `decimal` as a binary string, with each integer digit representing a binary digit. The resulting binary string is then prepended and appended with the string `'db'` to ensure the output has the desired format.