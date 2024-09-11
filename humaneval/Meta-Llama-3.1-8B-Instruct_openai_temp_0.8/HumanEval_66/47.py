```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of only uppercase characters in a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of ASCII codes of uppercase characters in the input string.
    """
    # Use a generator expression within the sum function to iterate over each character in the string
    # Check if the character is an uppercase letter using the isupper method and the ASCII code is a digit
    # Python's built-in ord function returns the Unicode code point for a given character
    return sum(ord(c) for c in s if c.isupper())

# Test the function with the given examples
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```