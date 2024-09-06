Here's a Python code block that contains a function called `decimal_to_binary` which takes a decimal number as input and returns the binary representation of that number with extra "db" characters at the beginning and end of the string:
```python
def decimal_to_binary(decimal):
    bin_str = bin(decimal)[2:]
    return "db" + bin_str + "db"

# Example usage:
decimal_value = 15
result = decimal_to_binary(decimal_value)
print(result)
```

In this script, the `decimal_to_binary` function takes a decimal number as input and uses the `bin` function to convert the decimal number to a binary number. The `bin` function returns a string consisting of `0b` followed by the binary representation of the number, so we use `bin(decimal)[2:]` to skip the `0b` part. The function then adds the extra characters "db" at the beginning and end of the string and returns the modified string.

When we run the example with `decimal_value = 15`, the output will be:
```
db1111db
```

This solution is straightforward and effectively converts decimal numbers to binary representation with the specified formatting.