Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    binary_str = '{:b}'.format(decimal)
    return 'db' + binary_str + 'db'

# Examples:
print(decimal_to_binary(15)) # prints 'db1111db'
print(decimal_to_binary(32))  # prints 'db100000db'
```

This script provides a function called `decimal_to_binary` that takes a decimal number as its argument and returns the binary representation of that number according to the problem description. The function uses the format specifier `{:b}` to convert the decimal number to a binary string, and then adds the prefix 'db' (as specified in the problem) to the front and back of the string for visualization purposes.