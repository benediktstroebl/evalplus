Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]    
    return f"db{binary}db"
```
This script defines a function `decimal_to_binary` that takes a decimal number as input and converts it to its binary representation. It uses the built-in `bin` function to convert the decimal number to a binary string, excluding the '0b' prefix. Then, it appends the prefixes "db" at the beginning and end of the string to meet the specified requirement. 

This solution adheres to the provided problem statement and can be used as a direct implementation for converting decimal numbers to binary strings. Feel free to adapt this code to your needs or explore different aspects of binary conversion! Let me know if you would like me to explain any part of the solution or provide additional insights.