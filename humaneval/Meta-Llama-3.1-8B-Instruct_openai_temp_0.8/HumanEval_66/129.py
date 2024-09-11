```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper characters in the string.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

In this script, the `digitSum` function uses a generator expression to iterate over each character `c` in the input string `s`. The `ord` function is used to get the ASCII code of each character. The `isupper` method is used to check if the character is uppercase. The `sum` function is then used to add up the ASCII codes of the upper characters.