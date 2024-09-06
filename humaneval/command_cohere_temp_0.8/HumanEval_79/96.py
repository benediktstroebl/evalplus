Here's a Python script with a self-contained function that solves the decimal-to-binary problem and passes the tests:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return f"db{binary}db"
```
This script defines a function `decimal_to_binary` that takes in a decimal number as input and converts it to its binary representation, with extra "db" characters added at the beginning and end for formatting. 

The function then returns the formatted binary string. You can use this function to convert any decimal number to binary by calling it and passing the decimal number as an argument.