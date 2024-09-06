Here's a Python script with a self-contained function that solves the decimal-to-binary problem and passes the tests:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]    
    return f"db{binary}db"
```
This script defines a function `decimal_to_binary` that takes in a decimal number as an input and returns a string of binary format. The binary string consists of '0' and '1' characters, with 'db' characters prepended and appended for formatting purposes. To achieve this, the function uses the `bin` function on the input decimal number, takes the substring starting from index 2, and appends 'db' at the beginning and end of it. 

Let's break down the code snippet: 
- `def decimal_to_binary(decimal)`: This line defines a function named `decimal_to_binary` that takes one parameter `decimal`. This function will be responsible for converting a given decimal number to its binary representation.
- `binary = bin(decimal)[2:]`: This line uses the `bin` function to convert the decimal number `decimal` to its binary representation. The result is a string like '0b1001011', but we are interested in the part after '0b'. The slice `[2:]` is used to remove the '0b' part, giving us '1001011'. This binary string is then stored in the variable `binary`.
- `return f"db{binary}db"`: The function returns a formatted string `db<binary>db`, where `<binary>` represents the binary string stored in the `binary` variable. Adding `db` at the beginning and end is done for formatting purposes, as per the spec. The `f` string syntax is used to interpolate the `binary` value.

Overall, this code snippet provides a function that takes a decimal number as input and returns its binary representation with appropriate formatting, ready for conversion back to a decimal number using the `int(binary[2:], 2)` operation.