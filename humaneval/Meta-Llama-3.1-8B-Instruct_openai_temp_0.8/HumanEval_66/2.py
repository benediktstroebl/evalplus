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

This script defines a function `digitSum` that takes a string `s` as input and returns the sum of ASCII codes of upper characters. It uses a generator expression within the built-in `sum` function to calculate the sum. The `ord` function is used to get the ASCII code of each character, and `isupper` method is used to check if a character is uppercase. The test cases at the end of the script demonstrate the function's correctness.