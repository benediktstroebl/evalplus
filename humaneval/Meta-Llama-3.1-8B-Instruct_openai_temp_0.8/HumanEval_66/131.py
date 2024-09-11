```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the upper characters only ASCII codes.

    Examples:
        >>> digitSum("")
        0
        >>> digitSum("abAB")
        131
        >>> digitSum("abcCd")
        67
        >>> digitSum("helloE")
        69
        >>> digitSum("woArBld")
        131
        >>> digitSum("aAaaaXa")
        153
    """
    sum = 0
    for char in s:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Add the ASCII value of the character to the sum
            sum += ord(char)
    return sum

# Test the function
print(digitSum(""))  # Expected output: 0
print(digitSum("abAB"))  # Expected output: 131
print(digitSum("abcCd"))  # Expected output: 67
print(digitSum("helloE"))  # Expected output: 69
print(digitSum("woArBld"))  # Expected output: 131
print(digitSum("aAaaaXa"))  # Expected output: 153
```

This script defines a function `digitSum` that takes a string `s` as input, and returns the sum of the ASCII codes of the uppercase letters in the string. It uses the `isupper` method to check if a character is an uppercase letter, and the `ord` function to get its ASCII code. The function iterates over each character in the string, adds the ASCII code of uppercase letters to the sum, and returns the total sum.