```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case letters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper case letters in the string.
    """
    sum_of_ascii = 0
    for char in s:
        # Check if the character is an upper case letter
        if char.isupper():
            # Add the ASCII code of the character to the sum
            sum_of_ascii += ord(char)
    return sum_of_ascii

# Test cases
print(digitSum(""))  # Expected output: 0
print(digitSum("abAB"))  # Expected output: 131
print(digitSum("abcCd"))  # Expected output: 67
print(digitSum("helloE"))  # Expected output: 69
print(digitSum("woArBld"))  # Expected output: 131
print(digitSum("aAaaaXa"))  # Expected output: 153
```

This script defines a function `digitSum` that takes a string `s` as input and returns the sum of ASCII codes of upper case letters in the string. It iterates over each character in the string, checks if it's an upper case letter using the `isupper` method, and if so, adds its ASCII code (obtained using the `ord` function) to the sum. The script also includes test cases to verify the correctness of the function.