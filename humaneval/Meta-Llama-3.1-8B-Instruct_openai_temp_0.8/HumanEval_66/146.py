```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of ASCII codes of upper case characters in the string.
    """
    # Initialize a variable to store the sum of ASCII codes
    ascii_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an upper case letter
        if char.isupper():
            # Add the ASCII code of the upper case character to the sum
            ascii_sum += ord(char)
    
    # Return the sum of ASCII codes
    return ascii_sum

# Test cases
print(digitSum(""))  # Expected output: 0
print(digitSum("abAB"))  # Expected output: 131
print(digitSum("abcCd"))  # Expected output: 67
print(digitSum("helloE"))  # Expected output: 69
print(digitSum("woArBld"))  # Expected output: 131
print(digitSum("aAaaaXa"))  # Expected output: 153
```

This script defines a function `digitSum` that takes a string `s` as input and returns the sum of ASCII codes of upper case characters in the string. It uses the `ord` function to get the ASCII code of each character and checks if the character is an upper case letter using the `isupper` method of the string. The sum is then returned at the end. The test cases are at the end of the script.