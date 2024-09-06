Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal).replace('0b', 'db').rjust(len(str(decimal), '0'))
    return binary + 'db'

# Example usage:
decimal_value = 15
result = decimal_to_binary(decimal_value)
print(result)
```
This script defines a function `decimal_to_binary(decimal)` that takes a decimal number as input and converts it to binary format. It uses the `bin` function to convert the decimal number to a binary string, then replaces the "0b" prefix with "db" to achieve the specified format. The `rjust` method ensures the binary string is padded with '0's on the left if needed to match the length of the original decimal number. Finally, the function returns the formatted binary string preceded and followed by 'db' characters.

When you run the script with a specific `decimal_value`, it will output the binary representation in the desired format, demonstrating the conversion from decimal to binary.