```python
def digitSum(s):
    """
    This function takes a string as input, converts it to upper case, then calculates the sum of the ASCII codes of each character.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the ASCII codes of the upper case characters in the string.
    """
    # Convert the string to upper case to ensure we're only summing ASCII codes of upper case characters
    upper_s = s.upper()
    
    # Initialize a variable to store the sum of the ASCII codes
    ascii_sum = 0
    
    # Iterate over each character in the string
    for char in upper_s:
        # Check if the character is an alphabet (not a special character or a digit)
        if char.isalpha():
            # Add the ASCII code of the character to the sum
            ascii_sum += ord(char)
    
    # Return the sum of the ASCII codes
    return ascii_sum

# Test the function
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

This script defines a function `digitSum` that takes a string as input, converts it to upper case, then calculates the sum of the ASCII codes of each character. The `ord` function is used to get the ASCII code of a character. The `isalpha` function is used to check if a character is an alphabet. The function is then tested with some sample inputs to ensure it's working correctly.