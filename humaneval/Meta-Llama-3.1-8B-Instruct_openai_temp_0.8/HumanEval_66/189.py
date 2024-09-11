```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper characters in a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of ASCII codes of upper characters.
    """
    # Initialize sum variable to 0
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

This script defines a function `digitSum` that iterates over each character in the input string. If the character is an uppercase letter, its ASCII code is added to the total sum. Finally, the function returns the total sum. The test cases at the end of the script demonstrate the function's behavior with different inputs.