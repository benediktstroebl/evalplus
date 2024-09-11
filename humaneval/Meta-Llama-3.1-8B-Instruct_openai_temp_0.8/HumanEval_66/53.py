```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of ASCII codes of upper case characters.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
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

This script defines a function `digitSum` that calculates the sum of ASCII codes of upper case characters in a string. It uses a generator expression to iterate over each character in the string, and the `ord` function to get the ASCII code of each character. The `isupper` method is used to filter out lower case characters. The script also includes test cases to verify that the function works correctly.