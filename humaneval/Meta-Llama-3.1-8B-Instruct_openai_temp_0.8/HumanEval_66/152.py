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

This script defines the `digitSum` function which uses a generator expression to iterate over each character in the string `s`. The `ord` function is used to get the ASCII value of each character, and the `isupper` method is used to check if the character is uppercase. If it is, its ASCII value is included in the sum. The sum is then returned. The test cases at the end of the script demonstrate the function's behavior.