```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only' ASCII codes.

    Args:
        s (str): Input string.

    Returns:
        int: Sum of ASCII codes of upper characters in the string.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # => 0
print(digitSum("abAB"))  # => 131
print(digitSum("abcCd"))  # => 67
print(digitSum("helloE"))  # => 69
print(digitSum("woArBld"))  # => 131
print(digitSum("aAaaaXa"))  # => 153
```

In this script, the `digitSum` function uses a generator expression to iterate over each character in the input string `s`. The `ord` function is used to get the ASCII code of each character, and the `isupper` method is used to check if a character is uppercase. The `sum` function is then used to calculate the sum of the ASCII codes of the uppercase characters. The test cases at the end of the script demonstrate the function's correctness.