```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only' ASCII codes.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of ASCII codes of upper characters in the string.
    """
    return sum(ord(char) for char in s if char.isupper())

# Test cases
print(digitSum(""))  # Expected output: 0
print(digitSum("abAB"))  # Expected output: 131
print(digitSum("abcCd"))  # Expected output: 67
print(digitSum("helloE"))  # Expected output: 69
print(digitSum("woArBld"))  # Expected output: 131
print(digitSum("aAaaaXa"))  # Expected output: 153
```

This script defines a function `digitSum` that takes a string `s` as input. It uses a generator expression to iterate over characters in the string. The `ord` function is used to get the ASCII value of each character, and the `isupper` method is used to check if the character is uppercase. The `sum` function is used to calculate the sum of ASCII codes of upper characters. The test cases are also included in the script to verify the correctness of the function.