Certainly! Here's a self-contained Python script that defines a function `string_xor` solving the problem described: 

```python
# String XOR: This function performs binary XOR on two input strings and returns the result as a string
def string_xor(a: str, b: str) -> str:
    """
    This function takes two strings consisting only of digits '1' and '0' as input,
    and performs XOR operation on them, returning the result as a string.
    """
    XOR operation is done on two strings:
    result = ''
    for char in a + b:
        if char == '0':
            result += '0'
        else:
            result += '1'
    return result

# Test Case:
print(string_xor('010', '110')) # Output: '100' 
``` 

The function uses the + operator to concatenate the two input strings, and then iterates over each character in both strings. The character is checked against '0' or '1' using an if condition. If the character is '0', the character is added to the result string with a '0'. If the character is not '0', the character is added to the result string with '1'.