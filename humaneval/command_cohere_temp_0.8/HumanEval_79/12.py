Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_string = bin(decimal)[2:]
    return f"db{binary_string}db"

# Example usage:
decimal_value = 15
result = decimal_to_binary(decimal_value)
print(result)
```

The provided example usage outputs:
```
db1111db
```

This code block contains a function `decimal_to_binary` that takes a decimal number as input and converts it to its binary representation, with extra "db" characters added at the beginning and end for formatting purposes. The `bin` function is used to convert the decimal number to a binary string, and the `[]` notation is used to remove the '0b' prefix.  Finally, it showcases how the function can be used to convert a decimal value to binary.