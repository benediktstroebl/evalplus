```markdown
**digitSum Function**
=====================

This function calculates the sum of ASCII codes of uppercase characters in a given string.

```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of ASCII codes of uppercase characters in the string.
    """
    
    # Initialize sum to 0
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Add the ASCII code of the character to the total sum
            total_sum += ord(char)
    
    # Return the total sum
    return total_sum

# Test cases
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

In this code, the `ord()` function is used to get the ASCII code of each character, and the `isupper()` method is used to check if a character is uppercase. The sum of the ASCII codes of uppercase characters is then returned by the function.