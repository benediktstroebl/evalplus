```python
def digitSum(s):
    """
    This function takes a string as input, filters out lower case letters, 
    calculates the ASCII value of each character, and returns their sum.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of ASCII values of upper case letters in the string.
    """
    # Initialize sum to zero
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an upper case letter
        if char.isupper():
            # Add the ASCII value of the character to the total sum
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