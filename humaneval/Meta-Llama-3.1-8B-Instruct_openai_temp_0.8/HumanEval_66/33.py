```python
def digitSum(s):
    """
    This function calculates the sum of the upper case ASCII codes in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the upper case ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    return sum(ord(char) for char in s if char.isupper())

# Test the function
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script uses the built-in Python functions `ord()` to get the ASCII code of a character and `isupper()` to check if a character is upper case. The `sum()` function is used to calculate the sum of the ASCII codes of the upper case characters in the string. The script also includes test cases to verify the correctness of the function.