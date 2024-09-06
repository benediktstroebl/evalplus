Here's a Python script that solves the problem:
```python
def decimal_to_binary(decimal):
    """Returns binary string for given decimal number with 'db' borders"""
    bin_num = bin(decimal)[2:]
    return f"db{bin_num}db"
```

The function `decimal_to_binary` takes a decimal number as an input and converts it to a binary string. It uses the built-in `bin` function to convert the decimal number to a binary number. The `[2:]` slice is used to remove the '0b' prefix. Then, it returns a string with the binary number surrounded by 'db' brackets. 

This code should be self-contained and can be executed directly to test it. 
For example:
```python
print(decimal_to_binary(15)) # db1111db
print(decimal_to_binary(32))  # db100000db
```

The output will be:
```
db1111db
db100000db
``` 

This script addresses the problem statement and aligns with the specified function specification. It is encapsulated and ready for use as a standalone module.