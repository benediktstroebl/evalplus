```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of only upper case letters in a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of ASCII codes of upper case letters in the string.
    """
    # Use a generator expression to iterate over each character in the string
    # Use the isupper() method to check if a character is upper case
    # Use the ord() function to get the ASCII code of each upper case character
    # Sum up the ASCII codes using the built-in sum() function
    return sum(ord(c) for c in s if c.isupper())

# Test the function
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

This script defines a function `digitSum` that takes a string `s` as input and returns the sum of the ASCII codes of all upper case letters in the string. It uses a generator expression to iterate over the characters in the string, checking each one for upper case using the `isupper()` method and summing up the ASCII codes of the upper case characters using the `ord()` function and the `sum()` function. The script then tests the function with several example inputs.