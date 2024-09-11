```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only' 
    ASCII codes.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the upper characters' ASCII codes.
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

This script uses a generator expression to iterate over each character in the string, and the `ord` function to get the ASCII code of each character. The `isupper` method is used to check if a character is uppercase, and only those characters are included in the sum.