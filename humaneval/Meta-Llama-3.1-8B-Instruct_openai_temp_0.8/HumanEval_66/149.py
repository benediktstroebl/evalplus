```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only' ASCII codes.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the upper characters only' ASCII codes.
    """
    # Initialize sum to 0
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Add the ASCII code of the character to the total sum
            total_sum += ord(char)
    
    # Return the total sum
    return total_sum

# Test cases
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```