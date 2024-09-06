Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided Markdown code block:
```python
def decimal_to_binary(decimal):
    binary_string = bin(decimal)[2:]
    return f"db{binary_string}db"

# Test Cases
assert decimal_to_binary(15) == "db1111db"
assert decimal_to_binary(32) == "db100000db"
```

This script defines a function `decimal_to_binary` that takes a decimal number as input and converts it to its binary representation, with extra "db" characters added at the beginning and end for formatting. The `bin` function is used to get the binary representation of the decimal number, and the result is trimmed to remove leading '0b' and trailing 'b' characters. Test cases are provided to verify the function's behavior against expected outputs. 

Let's break down the code step by step:
1. **Function Definition**:
   ```python
   def decimal_to_binary(decimal):
       ```
   This line defines a function named `decimal_to_binary` that takes a single parameter `decimal`, which is the decimal number you want to convert to binary.
2. **Binary Conversion**:
   ```python
   binary_string = bin(decimal)[2:]
   ```
   Here, the `bin` function is used to convert the decimal number `decimal` to its binary representation. The result starts with '0b' and ends with 'b', so we use `[2:` to slice away the leading and trailing characters. This gives us a string of binary digits without the extra characters.
3. **Formatting with "db"**:
   ```python
   return f"db{binary_string}db"
   ```
   To add the extra "db" characters for formatting, we use an f-string (`f"..."`) and concatenate the "db" prefixes and suffixes with the binary string.
4. **Test Cases**:
   ```python
   assert decimal_to_binary(15) == "db1111db"
   assert decimal_to_binary(32) == "db100000db"
   ```
   These lines test the `decimal_to_binary` function with two different input values (15 and 32) and verify that the output matches the expected formatted binary strings.

In summary, this script provides a self-contained function `decimal_to_binary` that solves the problem as outlined in the provided Markdown code block. You can use this function to convert any decimal number to a formatted binary string.