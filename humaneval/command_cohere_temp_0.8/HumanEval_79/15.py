Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_string = bin(decimal)[2:]
    return "db" + binary_string + "db"

# Example usage:
decimal_value = 15
result = decimal_to_binary(decimal_value)
print(result) 

```

This script defines a function `decimal_to_binary` that takes a decimal number as input and converts it to its binary representation, with extra 'db' characters added at the start and end for formatting. The example usage demonstrates how to use this function to convert the decimal value of 15 to binary format, resulting in 'db1111db'.