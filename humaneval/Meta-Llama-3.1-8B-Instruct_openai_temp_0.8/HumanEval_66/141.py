```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of the upper characters only ASCII codes.
    """
    # Initialize a variable to store the sum
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

This script defines a function `digitSum` that takes a string as input and returns the sum of the upper characters only ASCII codes. It uses a loop to iterate over each character in the string, checks if the character is an upper case letter using the `isupper` method, and adds the ASCII value of the character to the total sum if it is. Finally, it returns the total sum. The test cases are included at the end to verify the correctness of the function.