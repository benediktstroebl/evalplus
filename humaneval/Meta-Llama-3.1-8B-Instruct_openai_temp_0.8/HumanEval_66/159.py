```python
def digitSum(s):
    """
    This function calculates the sum of ASCII values of upper case characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII values of upper case characters.
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

In this script, the `ord` function is used to get the ASCII value of each character. The `isupper` method is used to check if a character is upper case. The `sum` function is used to calculate the sum of the ASCII values of the upper case characters. The test cases are provided to demonstrate the function's usage.