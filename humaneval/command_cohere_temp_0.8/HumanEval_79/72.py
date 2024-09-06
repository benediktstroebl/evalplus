Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return f"db{binary}db"
```
This code defines a function `decimal_to_binary` that takes a decimal number as input and converts it to its binary representation. It uses the built-in `bin` function to get the binary representation of the decimal number, excluding the leading '0b' part. The result is then prefixed with 'db' (as per the problem statement) to ensure the output string has the desired format.

Let's break it down with the help of an example:
```python
decimal_to_binary(15)
# Returns "db1111db"
```
In this case, the binary representation of 15 is '1111'. The function prefaces this with 'db' to get the desired output.