```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters' ASCII codes.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the upper characters' ASCII codes.
    """
    return sum(ord(char) for char in s.upper() if char.isalpha())

# Test cases
print(digitSum(""))  # => 0
print(digitSum("abAB"))  # => 131
print(digitSum("abcCd"))  # => 67
print(digitSum("helloE"))  # => 69
print(digitSum("woArBld"))  # => 131
print(digitSum("aAaaaXa"))  # => 153
```

This script defines a function `digitSum` that calculates the sum of the ASCII codes of upper case characters in the given string. The function uses a generator expression to iterate over the characters in the string, converts each character to upper case, checks if the character is an alphabet letter using `isalpha()`, and sums up the ASCII codes of the upper case letters using `ord()`. The result is returned as an integer.