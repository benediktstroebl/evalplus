Here's a Python script with a self-contained function that solves the decimal-to-binary problem and passes the tests:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]    
    return f"db{binary}db"
```
This code defines a function `decimal_to_binary` that takes a decimal number as input and converts it to its binary representation, with extra "db" characters added at the beginning and end for formatting. 

The `bin` function converts the decimal number to a binary string, and the `[2:]` slice is used to remove the initial '0b' part of the binary string. 

Overall, this code provides an efficient solution to the problem, and its output can be directly used by calling the `decimal_to_binary` function with the desired decimal number.  This will help accomplish the task of converting decimal numbers to binary representations.  If you have any questions, let's dive deeper!