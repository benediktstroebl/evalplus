Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided Markdown code block:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]    
    return f"db{binary}db"
```
This function takes a decimal number as input and converts it to its binary representation. It uses the `bin` function to get the binary representation of the decimal number, excluding the leading '0b' part. The resulting binary string is then prepended and appended with the characters 'db' to ensure the desired output format. The function returns the binary string encapsulated by 'db' characters, ready for interpretation. 

This solution directly addresses the task as presented in the Markdown code block. It's worth noting that this function assumes the input decimal number is valid and within the acceptable range for integer values in Python.