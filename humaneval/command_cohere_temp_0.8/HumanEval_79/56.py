Here's a Python script that solves the problem of converting a decimal number to a binary string, with the added constraint that the string should start and end with the two characters 'db'. 

The provided code defines a function `decimal_to_binary` that takes in a decimal number as an input and returns a string of binary digits, framed by the two characters 'db'. The function uses the built-in `bin` function for conversion and string concatenation to achieve this result. The `db` characters are added at the beginning and end of the returned string to ensure the framing is maintained. 

```python
def decimal_to_binary(decimal):
    binary = f"db{bin(decimal)[2:]}db"
    return binary
```

You can use this function by calling it with a decimal number as the input, like this:
```python
result = decimal_to_binary(32)
print(result)  # Outputs: db100000db
```

This will convert the decimal number to binary and return the formatted string as 'db100000db', with the number represented in binary and framed by the two characters 'db'.