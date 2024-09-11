```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper case characters' ASCII codes.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the upper case characters' ASCII codes.
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

This script uses a generator expression to iterate over the characters in the input string `s`. The `ord` function is used to get the ASCII code of each character. The `isupper` function is used to check if a character is upper case. The `sum` function is used to add up the ASCII codes of the upper case characters.