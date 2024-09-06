Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_str = "{0:b}".format(decimal)
    return "db{0}db".format(binary_str)
```
This script provides a function called `decimal_to_binary` that takes a decimal number as its input and returns a string representing the binary equivalent. It uses the `format` function with a binary prefix ('b') to convert the decimal number to a binary string, and then uses string formatting to prepend and append 'db' to the binary string to ensure the output matches the specified format. 

To use this script, you can simply call the `decimal_to_binary` function with a decimal number as follows:
```python
result = decimal_to_binary(15)
print(result)  # Outputs: db1111db
```
This will convert the decimal number 15 to the corresponding binary string "db1111db" as specified in the problem statement.