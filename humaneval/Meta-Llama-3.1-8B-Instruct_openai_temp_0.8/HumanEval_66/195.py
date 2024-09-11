```python
def digitSum(s):
    """
    This function calculates the sum of the ASCII codes of upper case characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the ASCII codes of upper case characters.
    """
    return sum(ord(char) for char in s if char.isupper())

# Test cases
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

This script defines a function `digitSum` that uses a generator expression to iterate over each character in the input string `s`. The `ord` function is used to get the ASCII code of each character, and the `isupper` method is used to check if the character is an uppercase letter. The `sum` function is then used to calculate the sum of the ASCII codes of the uppercase characters.