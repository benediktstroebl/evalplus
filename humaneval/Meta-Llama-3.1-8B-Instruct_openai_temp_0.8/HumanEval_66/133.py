```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of the upper characters only ASCII codes.
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

In this script, the `ord(char)` function is used to get the ASCII value of each character in the string. The `isupper()` method is used to check if a character is uppercase. If a character is uppercase, its ASCII value is added to the sum. If not, it is skipped.