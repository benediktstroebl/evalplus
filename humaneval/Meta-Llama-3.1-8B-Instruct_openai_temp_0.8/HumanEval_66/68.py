```python
def digitSum(s):
    """
    This function calculates the sum of the ASCII codes of the upper case characters in a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of the ASCII codes of the upper case characters.
    """
    # Initialize the sum to 0
    total = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an upper case letter
        if char.isupper():
            # Add the ASCII code of the character to the total
            total += ord(char)
    
    # Return the total sum
    return total

# Test the function with the provided examples
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```