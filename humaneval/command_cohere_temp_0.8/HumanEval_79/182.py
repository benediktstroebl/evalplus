Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_str = "{0:b}".format(decimal)
    return "db{0}db".format(binary_str)

# Example usage:
decimal_value = 15
result = decimal_to_binary(decimal_value)
print(result)
```
This script incorporates the specified extra "db" characters before and after the binary number. The format specification `{0:b}` is used to convert the decimal number to a binary string, and then the "db" characters are added to the beginning and end of the string. Finally, the formatted binary string is printed. 

When the example decimal value of 15 is passed to the `decimal_to_binary` function, the resulting output will be "db1111db" as stipulated in the problem description.