```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.

    Parameters:
    s (str): Input string

    Returns:
    int: Sum of the upper characters only ASCII codes
    """
    return sum(ord(c) for c in s if c.isupper())

# Test the function
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

In this script, the `ord()` function is used to get the ASCII code of each character in the string, and the `isupper()` function is used to check if the character is an uppercase letter. The `sum()` function is used to calculate the sum of the ASCII codes of the uppercase characters.