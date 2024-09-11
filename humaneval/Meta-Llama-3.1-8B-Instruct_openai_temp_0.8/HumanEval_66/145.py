```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the ASCII codes of its upper characters.

    Parameters:
    s (str): Input string.

    Returns:
    int: Sum of ASCII codes of the upper characters in the string.
    """
    return sum(ord(char) for char in s if char.isupper())

# Test cases
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script defines a function `digitSum` that takes a string `s` as input and returns the sum of the ASCII codes of its upper characters. The `ord` function is used to get the ASCII code of each character, and the `isupper` method is used to filter out the upper characters. The result is calculated using a generator expression within the `sum` function. The test cases are included at the end to demonstrate the functionality of the function.