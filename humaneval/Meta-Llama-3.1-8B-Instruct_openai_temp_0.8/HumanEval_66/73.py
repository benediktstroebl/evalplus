```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a given string.

    Args:
    s (str): The input string.

    Returns:
    int: The sum of ASCII codes of upper case characters in the string.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

This script defines a function `digitSum` that calculates the sum of ASCII codes of upper case characters in a given string. It uses a generator expression inside the built-in `sum` function to iterate over the characters in the string, check if each character is upper case using the `isupper` method, and calculate the ASCII code using the `ord` function. The result is then printed for the provided test cases.