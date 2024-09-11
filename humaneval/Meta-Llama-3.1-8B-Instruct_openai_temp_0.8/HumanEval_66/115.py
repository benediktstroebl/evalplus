```python
def digitSum(s):
    """
    This function calculates the sum of the ASCII codes of upper case letters in a given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the ASCII codes of upper case letters.
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

This script defines a function `digitSum` that takes a string `s` as input. The function uses a generator expression to iterate over each character `c` in the string. The `ord` function is used to get the ASCII code of each character, and the `isupper` function is used to check if the character is an upper case letter. The `sum` function is then used to add up the ASCII codes of all the upper case letters. The result is returned by the function.

The test cases at the end of the script demonstrate the function's behavior with different inputs.