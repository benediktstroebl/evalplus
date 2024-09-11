```python
def digitSum(s):
    """
    This function calculates the sum of the ASCII codes of only the upper case characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the ASCII codes of the upper case characters in the string.
    """
    # Use a generator expression to iterate over each character in the string
    # and only keep the ones that are upper case by checking their ASCII value
    # Then, sum up the ASCII values of these characters
    return sum(ord(c) for c in s if 'A' <= c <= 'Z')


# Test cases
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script defines a function `digitSum` that takes a string `s` as input and returns the sum of the ASCII codes of only the upper case characters in the string. It uses a generator expression to iterate over each character in the string, and only keeps the ones that are upper case by checking their ASCII value. Finally, it sums up the ASCII values of these characters and returns the result.