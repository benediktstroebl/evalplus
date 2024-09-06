Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]    
    return f"db{binary}db"
```
This function takes a decimal number as input and converts it to its binary representation. The `bin` function gives the binary representation of a number, but we extract it from the returned string with `bin(decimal)[2:]`. We then add "db" at the beginning and end to fulfill the problem's specification. 

Here's how you can test this function:
```python
assert decimal_to_binary(15) == "db1111db"
assert decimal_to_binary(32) == "db100000db"
```

This script ensures the function works as per the given problem statement and provides a reliable solution for converting decimal numbers to binary strings.