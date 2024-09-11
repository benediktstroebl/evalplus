```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper characters in a given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of ASCII codes of upper characters in the string.

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
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

In this script, the `digitSum` function uses a generator expression to iterate over each character in the string `s`. The `isupper` method is used to check if a character is uppercase, and the `ord` function is used to get the ASCII code of a character. The `sum` function is then used to add up the ASCII codes of all upper characters in the string. The test cases at the end of the script demonstrate the function's behavior with different inputs.