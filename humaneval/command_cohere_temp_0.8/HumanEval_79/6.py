Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_str = "{0:b}".format(decimal)
    return "db{0}db".format(binary_str)

# Example usage:
decimal_value = 15
converted_value = decimal_to_binary(decimal_value)
print(f"Converted {decimal_value} to {converted_value}")
```
This script defines a function `decimal_to_binary` that takes a decimal number as input and converts it to binary format according to the problem statement. The function uses the formatting specifier `{0:b}` to convert the decimal number to a binary string, where `b` specifies binary format. Finally, it prefaces and appends this binary string with "db" to ensure the output has the desired format. 

You can verify the functionality of the script by executing the example usage provided in the comment. Note that the example usage produces output comprising special characters, such as `db1111db`, so the output may need to be inspected carefully or with suitable formatting in the console. If the console output isn't readable, you may want to consider printing the result to a file.