```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper characters in a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of ASCII codes of upper characters in the string.
    """
    
    # Initialize sum to 0
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an upper case letter
        if char.isupper():
            # Add the ASCII value of the character to the sum
            total_sum += ord(char)
    
    # Return the total sum
    return total_sum

# Test cases
print(digitSum(""))  # Expected output: 0
print(digitSum("abAB"))  # Expected output: 131
print(digitSum("abcCd"))  # Expected output: 67
print(digitSum("helloE"))  # Expected output: 69
print(digitSum("woArBld"))  # Expected output: 131
print(digitSum("aAaaaXa"))  # Expected output: 153
```

This script defines a function `digitSum` that calculates the sum of ASCII codes of upper characters in a given string. It iterates over each character in the string, checks if the character is an upper case letter using the `isupper` method, and adds the ASCII value of the character to the sum if it is. The script includes test cases to demonstrate the function's behavior.