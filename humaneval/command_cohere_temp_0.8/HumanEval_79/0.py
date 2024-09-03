Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the given specification:
```python
def decimal_to_binary(decimal):
    binary_str = "{0:b}".format(decimal)
    return "db{0}db".format(binary_str)
```
This function takes a decimal number `decimal` as input and converts it to its binary representation. It uses the `format` function with a binary prefix (`'b'`) to directly convert the decimal number to a binary string. 

The returned binary string is then prefixed with "db" (as per the specification) to ensure the output format meets the requirement. The `db` prefixes are added at the beginning and end of the string. 

The function is self-contained and can be directly executed to perform the desired conversion from decimal to binary.  It's also important to note that this solution is efficient since it utilizes built-in string methods, ensuring both accuracy and performance.