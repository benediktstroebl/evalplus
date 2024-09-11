```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only' ASCII codes.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of the upper characters only' ASCII codes.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # Expected output: 0
print(digitSum("abAB"))  # Expected output: 131
print(digitSum("abcCd"))  # Expected output: 67
print(digitSum("helloE"))  # Expected output: 69
print(digitSum("woArBld"))  # Expected output: 131
print(digitSum("aAaaaXa"))  # Expected output: 153
```

This script defines a function `digitSum` that calculates the sum of the ASCII codes of upper-case characters in a given string using a generator expression. The `isupper` method is used to filter out lower-case characters. The `ord` function is used to get the ASCII code of each character. The `sum` function adds up these ASCII codes. The test cases at the end demonstrate the function's behavior with different inputs.