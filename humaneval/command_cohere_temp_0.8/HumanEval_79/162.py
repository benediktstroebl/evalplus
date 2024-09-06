Here's a Python code block that contains a function called `decimal_to_binary` which takes a decimal number as input and returns the binary representation of that number with extra characters 'db' at the beginning and end of the string for formatting purposes. 

The function contains an example showing how the function can be used in the following way:
```python
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    # converting decimal to binary
    binary = bin(decimal)[2:]
    # adding 'db' at the beginning and end for formatting
    return 'db' + binary + 'db'

# Example:
decimal_number = 15
result = decimal_to_binary(decimal_number)
print(result)
```

To test the function, we can perform the following step:
```python
# Driver Code
decimal_number = 15
result = decimal_to_binary(decimal_number)
print(result)
```

This will produce the following result: 
```
db1111db
```

The script also contains comments that explain the functionality and purpose of each line of code contained therein.