```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper characters.
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

This script defines a function `digitSum` that uses a generator expression to iterate over the characters in the input string `s`. The `ord` function is used to get the ASCII code of each character, and the `isupper` method is used to check if the character is an uppercase letter. The `sum` function is then used to add up the ASCII codes of the upper characters. The test cases are also included to demonstrate the function's behavior.