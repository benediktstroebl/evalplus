```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only' 
    ASCII codes.

    Parameters:
    s (str): The input string

    Returns:
    int: The sum of the upper characters only' ASCII codes
    """
    # Initialize the sum to 0
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Add the ASCII code of the character to the total sum
            total_sum += ord(char)
    
    # Return the total sum
    return total_sum

# Test the function with the provided examples
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script defines the `digitSum` function, which iterates over each character in the input string. If the character is an uppercase letter, it adds the ASCII code of the character to the total sum. The function then returns the total sum. The script also includes test cases to verify that the function works correctly for the provided examples.